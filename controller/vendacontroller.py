from db.vendadb import VendaDB
from model.venda import Venda


class VendaController:
    def cadastrarVenda(self,medico,comprador,endereco,usuario,lote):
        todas = self.listarVenda()
        ultima = todas.pop()
        idVenda = int(ultima.idVenda) + 1
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

    def listarVenda(self):
        db = VendaDB()
        vendas = db.retornaVendas()
        return vendas
        
