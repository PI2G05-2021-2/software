from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem,MDList

from controller.vendacontroller import VendaController


class HomeEmpresaScreen(MDScreen):

    screen = MDScreen()
    vendas = VendaController.listarVenda()
    listView = MDList()
    i = 0
    while i < len(vendas):
        item = OneLineListItem(text=str(vendas[i].comprador.nomeComprador))
        listView.add_widget(item)
        i = i + 1
    
    screen.add_widget(listView)
    