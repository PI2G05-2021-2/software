from kivy.uix.screenmanager import ScreenManager
from screens.screens_acompanhar.acompanharscreen import AcompanharScreen
from screens.screens_login.loginscreen import LoginScreen
from screens.screens_laboratorio.laboratorioscreen import LaboratorioScreen
from screens.screens_perfil.perfilscreen import PerfilScreen
from screens.screens_empresa.homeempresascreen import HomeEmpresaScreen
from screens.screens_empresa.registroempresascreen import RegistroEmpresaScreen


sm = ScreenManager()
sm.add_widget(LoginScreen())
sm.add_widget(LaboratorioScreen())
sm.add_widget(AcompanharScreen())
sm.add_widget(PerfilScreen())
sm.add_widget(HomeEmpresaScreen())
sm.add_widget(RegistroEmpresaScreen())

class MainScreenManager(ScreenManager):
    pass
