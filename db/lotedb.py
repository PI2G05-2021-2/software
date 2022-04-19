from collections import namedtuple
from db.criadb import CriaDB
from db.perfilExtracaodb import PerfilExtracaoDB
from db.usuariodb import UsuarioDB
from model.lote import Lote

class LoteDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB()

    def insereLote(self, lote):
        query = "INSERT INTO lote (idLote,fk_PerfilExtracao_idPerfil,fk_Usuario_login) VALUES(%s,%s,%s)"
        val = (lote.idLote,lote.perfil.idPerfil,lote.usuario.login) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()
    
    def encontraLote(self, idLote):
        self.criadb.instanciaDB(
            "SELECT * FROM lote WHERE idLote = %(id)s", {'id': idLote},False)
        dicionario = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
        lotetemp = namedtuple('lotetemp', dicionario.keys())(*dicionario.values())
        lote = Lote(lotetemp.idLote,PerfilExtracaoDB().encontraPerfilExtracao(lotetemp.fk_PerfilExtracao_idPerfil),
                    UsuarioDB().encontraUsuario(lotetemp.fk_Usuario_login2))
        return lote
    
    def atualizaLote(self,idLote, perfil, usuario):
        val = (perfil.idPerfil, usuario.login,idLote)
        self.criadb.instanciaDB("UPDATE lote SET fk_PerfilExtracao_idPerfil = %s, fk_Usuario_login = %s WHERE idLote = %s",val,True)
        self.criadb.fechaDB()

    def deletaLote(self,idLote):
        self.criadb.instanciaDB("DELETE FROM lote WHERE idLote = %(id)s", {'id': idLote},True)
        self.criadb.fechaDB()
    
    def retornaLotes(self):
        self.criadb.instanciaDB(
            "SELECT * FROM lote",None,False
        )
        dicionario = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        lotes = []
        i = 0
        while i<len(dicionario):
            lotetemp = namedtuple('lotetemp', dicionario[i].keys())(*dicionario[i].values())
            lote = Lote(lotetemp.idLote,PerfilExtracaoDB.encontraPerfilExtracao(lotetemp.fk_PerfilExtracao_idPerfil),
                    UsuarioDB.encontraUsuario(lotetemp.fk_Usuario_login))
            lotes.append(lote)
            i = i + 1 
        
        return lotes