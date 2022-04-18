
import os
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.uix.scrollview import ScrollView

Window.size = (414, 736)

# main app class for kaki app with kivymd modules


class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1  # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/mainscreenmanager.kv"),
        os.path.join(os.getcwd(), "screens/screens_login/loginscreen.kv"),
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


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
