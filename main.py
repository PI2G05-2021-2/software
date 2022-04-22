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
from model.usuario import Usuario
from screens.mainscreenmanager import MainScreenManager


Window.size = (414, 736)

leitura = []
currentUsuario : Usuario

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """
    
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

    def getAllVendas(self,listaVendas):
        vendas = VendaController().listarVenda()
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
        time.sleep(10)
        while True:
            conexao, endereco = sockobj.accept()
            conexao.send(perfil.encode())
            while True:
                data = conexao.recv(200)
                leitura.append(str(data.decode()))
                if data.decode() == '':
                    break
            fechou = conexao.close()
            if fechou == None:
                break
    
    def mostraTemperatura(self,teste):
        while True:
            if len(self.leitura)>0:
                ultimaLeitura = leitura.pop()
                dicionarioLeitura = ast.literal_eval(str(ultimaLeitura))
                extracao = namedtuple('extracao', dicionarioLeitura.keys())(*dicionarioLeitura.values())
                self.parent.ids.temperatura.text = extracao.TEMPERATURA

    def mostraTempo(self,teste):
        while True:
            if len(self.leitura)>0:
                ultimaLeitura = leitura.pop()
                dicionarioLeitura = ast.literal_eval(str(ultimaLeitura))
                extracao = namedtuple('extracao', dicionarioLeitura.keys())(*dicionarioLeitura.values())
                self.parent.ids.tempo.text = extracao.TEMPO

    def mostraPotencia(self,teste):
        while True:
            if len(self.leitura)>0:
                ultimaLeitura = leitura.pop()
                dicionarioLeitura = ast.literal_eval(str(ultimaLeitura))
                extracao = namedtuple('extracao', dicionarioLeitura.keys())(*dicionarioLeitura.values())
                self.parent.ids.potencia.text = extracao.POTENCIA
    
    def mostraVelocidade(self,teste):
        while True:
            if len(self.leitura)>0:
                ultimaLeitura = leitura.pop()
                dicionarioLeitura = ast.literal_eval(str(ultimaLeitura))
                extracao = namedtuple('extracao', dicionarioLeitura.keys())(*dicionarioLeitura.values())
                self.parent.ids.velocidade.text = extracao.VELOCIDADE

    def redireciona(self,perfil):
        dadosPerfil = PerfilExtracaoController().mostrarPerfilExtracao(perfil)
        lote = LoteController().cadastrarLote(dadosPerfil,self.currentUsuario)
        threading.Thread(target=self.iniciaWebSocket,args=perfil).start()
        threading.Thread(target=self.mostraTemperatura,args='None').start()
        threading.Thread(target=self.mostraTempo,args='None').start()
        threading.Thread(target=self.mostraPotencia,args='None').start()
        threading.Thread(target=self.mostraVelocidade,args='None').start()
        return 'acompanhar'

    def iniciaRelatorio(self):
        if len(leitura)>0:
            arq = open('relatorio.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
            pickle.dump(leitura,arq) #Grava uma stream do objeto "dic" para o arquivo.
            arq.close() #fechar o arquivo

# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
    
