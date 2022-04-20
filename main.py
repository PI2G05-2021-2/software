import os
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

from controller.compradorcontroller import CompradorController
from controller.lotecontroller import LoteController
from controller.medicocontroller import MedicoController
from controller.usuariocontroller import UsuarioController
from controller.vendacontroller import VendaController

from model.usuario import Usuario


Window.size = (414, 736)

if 'currentUsuario' not in globals():
    currentUsuario : Usuario


# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """
    DEBUG = 1  # set this to 0 make live app not working

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


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
