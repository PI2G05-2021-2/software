from collections import namedtuple
import os
import threading
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem,MDList,IconLeftWidget
from kivy.clock import Clock

from socket import *
import time
import ast
import pickle 

from controller.compradorcontroller import CompradorController
from controller.lotecontroller import LoteController
from controller.medicocontroller import MedicoController
from controller.perfilExtracaocontroller import PerfilExtracaoController
from controller.usuariocontroller import UsuarioController
from controller.vendacontroller import VendaController
from db.criadb import CriaDB
from model.lote import Lote
from model.usuario import Usuario
from screens.mainscreenmanager import MainScreenManager


Window.size = (414, 736)

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    currentUsuario : Usuario

    currentLote : Lote
    currentLote = LoteController().listarLote().pop()


    leitura = []
    
    DEBUG = 1  # set this to 0 make live app not working

    # Caso não tenha o banco de dados
    #db = CriaDB()
    #db.criaTabelas()

    # Cadastro dos Perfis de Extração
    perfis = []
    perfis = PerfilExtracaoController.listarPerfis()

    # A ordem é essa = TEMPERATURA,TEMPO,POTÊNCIA,VELOCIDADE
    if len(perfis) < 3:
        perfil1 = PerfilExtracaoController.cadastrarPerfilExtracao(5,20,2,30)
        perfil2 = PerfilExtracaoController.cadastrarPerfilExtracao(7,15,4,10)
        perfil3 = PerfilExtracaoController.cadastrarPerfilExtracao(3,10,1,50)
    else:
        perfil1 = PerfilExtracaoController().mostrarPerfilExtracao(0)
        perfil2 = PerfilExtracaoController().mostrarPerfilExtracao(1)
        perfil3 = PerfilExtracaoController().mostrarPerfilExtracao(2)

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/mainscreenmanager.kv"),
        os.path.join(os.getcwd(), "screens/screens_login/loginscreen.kv"),
        os.path.join(os.getcwd(), "screens/screens_perfil/perfilscreen.kv"),
        os.path.join(os.getcwd(), "screens/screens_laboratorio/laboratorioscreen.kv"),
        os.path.join(os.getcwd(), "screens/screens_empresa/registroempresascreen.kv"),
        os.path.join(os.getcwd(), "screens/screens_empresa/homeempresascreen.kv"),
        os.path.join(os.getcwd(), "screens/screens_acompanhar/acompanharscreen.kv")
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.mainscreenmanager",
        "LoginScreen": "screens.screens_login.loginscreen",
        "LaboratorioScreen": "screens.screens_laboratorio.laboratorioscreen",
        "AcompanharScreen": "screens.screens_acompanhar.acompanharscreen",
        "PerfilScreen": "screens.screens_perfil.perfilscreen",
        "HomeEmpresaScreen": "screens.screens_empresa.homeempresascreen",
        "RegistroEmpresaScreen": "screens.screens_empresa.registroempresascreen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Blue"
        return Factory.MainScreenManager()
    
    def login(self,usuario,senha,tipo):
        usr = UsuarioController.mostrarUsuario(usuario)
        if usr == None:
            popup = Popup(title='Erro',
                    content=Label(text='Usuário não encontrado'),
                    size_hint=(None, None), size=(200, 200))
            popup.open()
        else:
            if usr.senha != senha or usr.tipo != tipo:
                popup = Popup(title='Erro',
                        content=Label(text='Dados incorretos'),
                        size_hint=(None, None), size=(200, 200))
                popup.open()
            
            else:
                self.currentUsuario = usr
                if tipo == 'E':
                    return 'homeempresa'
                elif tipo == 'L':
                    return 'perfis'
                else:
                    popup = Popup(title='Erro',
                        content=Label(text='Dados incorretos'),
                        size_hint=(None, None), size=(200, 200))
                    popup.open()
    
    def novaVenda(self, nmComprador,telComprador,identComprador,crmSol,nmSol,telSol,cidComprador,enderecoVenda,loteVenda):
        if nmComprador == '' or telComprador == '' or identComprador == '':
            popup = Popup(title='Erro',
                content=Label(text='Preencha todos os campos!'),
                size_hint=(None, None), size=(210, 210))
            popup.open()
        elif crmSol == '' or nmSol == '' or telSol == '':
            popup = Popup(title='Erro',
                content=Label(text='Preencha todos os campos!'),
                size_hint=(None, None), size=(210, 210))
            popup.open()
        elif cidComprador == '' or enderecoVenda == '' or loteVenda == '':
            popup = Popup(title='Erro',
                content=Label(text='Preencha todos os campos!'),
                size_hint=(None, None), size=(210, 210))
            popup.open()
        else:
            comprador = CompradorController().cadastrarComprador(identComprador,telComprador,nmComprador,cidComprador)
            medico = MedicoController().cadastrarMedico(crmSol,telSol,nmSol)
            lote = LoteController().mostrarLote(loteVenda)
            venda = VendaController().cadastrarVenda(medico,comprador,enderecoVenda,self.currentUsuario,lote)
            return 'homeempresa'

    def getAllVendas(self,*args):
        vendas = VendaController().listarVenda()
        listaVendas = self.approot.get_screen('homeempresa').ids.listaVendas
        listaVendas.clear_widgets()
        for i in vendas:
            item = OneLineListItem(text=str(i.comprador.nomeComprador))
            #item.add_widget(IconLeftWidget(icon= "account-circle",theme_text_color= "Custom",text_color= self.theme_cls.primary_color))
            listaVendas.add_widget(item)

    def iniciaWebSocket(self,perfil:str):
        meuHost = 'localhost'
        minhaPort = 50007
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.bind((meuHost, minhaPort))
        sockobj.listen(5)
        fechou = 1
        #time.sleep(10)
        while True:
            conexao, endereco = sockobj.accept()
            conexao.send(perfil.encode())
            while True:
                data = conexao.recv(200)
                self.leitura.append(str(data.decode()))
                if data.decode() == '':
                    break
            fechou = conexao.close()
            if fechou == None:
                break
    
    def mostraStatus(self, *args):
        if len(self.leitura)>0:
            ultimaLeitura = self.leitura.pop()
            dicionarioLeitura = ast.literal_eval(str(ultimaLeitura))
            extracao = namedtuple('extracao', dicionarioLeitura.keys())(*dicionarioLeitura.values())
            #self.root.current = 'acompanhar'
            self.approot.get_screen('acompanhar').ids.temperatura.text = str(extracao.TEMPERATURA)
            self.approot.get_screen('acompanhar').ids.tempo.text = str(extracao.TEMPO)
            self.approot.get_screen('acompanhar').ids.potencia.text = str(extracao.POTENCIA)
            self.approot.get_screen('acompanhar').ids.velocidade.text = str(extracao.VELOCIDADE)
                
    def on_start(self):
        #threading.Thread(target=Clock.schedule_interval,args=(self.mostraStatus(),2)).start()
        #threading.Thread(target=self.mostraStatus)
        Clock.schedule_interval(self.mostraStatus,2)
        Clock.schedule_interval(self.getAllVendas,2)

    def redireciona(self,perfil):
        dadosPerfil = PerfilExtracaoController().mostrarPerfilExtracao(perfil)
        self.currentLote = LoteController().cadastrarLote(dadosPerfil,self.currentUsuario)
        threading.Thread(target=self.iniciaWebSocket,args=perfil).start()
        #threading.Thread(target=self.mostraStatus,args='None').start()
        return 'acompanhar'

    def iniciaRelatorio(self):
        if len(self.leitura)>0:
            arq = open('relatorio.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
            pickle.dump(self.leitura,arq) #Grava uma stream do objeto "dic" para o arquivo.
            arq.close() #fechar o arquivo

# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
    
