from db.lotedb import LoteDB
from model.lote import Lote


class LoteController:
    def cadastrarLote(idLote, perfil, usuario):
        lote = Lote(idLote, perfil, usuario)
        
        db = LoteDB()
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

    def listarLote():
        db = LoteDB()
        lotes = db.retornaLotes()
        return lotes
