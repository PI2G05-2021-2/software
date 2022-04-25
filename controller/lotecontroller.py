from db.lotedb import LoteDB
from model.lote import Lote


class LoteController:
    def cadastrarLote(self,perfil, usuario):
        db = LoteDB()
        lista = db.retornaLotes()
        if len(lista) == 0:
            idLote = 0
        else:
            ultimo = lista.pop()
            idLote = int(ultimo.idLote) + 1
        lote = Lote(idLote, perfil, usuario)
        db.insereLote(lote)
        return lote

    def editarLote(idLote, perfil, usuario):
        db = LoteDB()        
        db.atualizaLote(idLote, perfil, usuario)
        lote = Lote(idLote, perfil, usuario)
        return lote

    def excluirLote(idLote):
        db = LoteDB()
        db.deletaLote(idLote)

    def mostrarLote(self,idLote):
        db = LoteDB()
        lote = db.encontraLote(idLote)
               
        return lote

    def listarLote(self):
        db = LoteDB()
        lotes = db.retornaLotes()
        return lotes
