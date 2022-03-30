from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class JanelaGerenciadora(ScreenManager):
    pass


class PerfisdeExtracao(Screen):
    pass


class InformacoesDePerfis(Screen):
    pass


class AcompanharExtracao(Screen):
    pass


class aplicativo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Blue"
        return Builder.load_file('aplicativo.kv')


aplicativo().run()
