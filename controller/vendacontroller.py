from db.vendadb import VendaDB
from model.venda import Venda


class VendaController:
    def cadastrarVenda(idVenda,medico,comprador,endereco,usuario,lote):
        venda = Venda(idVenda,medico,comprador,endereco,usuario,lote)
        
        db = VendaDB()
        db.insereVenda(venda)

        return venda

    def editarVenda(idVenda,medico,comprador,endereco,usuario,lote):
        db = VendaDB()        
        db.atualizaVenda(idVenda,medico,comprador,endereco,usuario,lote)
        venda = Venda(idVenda,medico,comprador,endereco,usuario,lote)
        return venda

    def excluirVenda(idVenda):
        db = VendaDB()
        db.deletaVenda(idVenda)

    def mostrarVenda(idVenda):
        db = VendaDB()
        venda = db.encontraVenda(idVenda)
               
        return venda

    def listarVenda():
        db = VendaDB()
        vendas = db.retornaVendas()
        return vendas
        
