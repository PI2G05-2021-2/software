
import os
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager

from controller.usuariocontroller import UsuarioController


Window.size = (414, 736)


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
        os.path.join(os.getcwd(), "screens/screens_acompanhar/acompanharscreen.kv"),
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
                if tipo == 'E':
                    return 'homeempresa'
                elif tipo == 'L':
                    return 'perfis'
                else:
                    popup = Popup(title='Erro',
                        content=Label(text='Dados incorretos'),
                        size_hint=(None, None), size=(200, 200))
                    popup.open()



# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
