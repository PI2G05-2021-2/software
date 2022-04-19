from collections import namedtuple
from db.criadb import CriaDB

class CompradorDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB()  

    def insereComprador(self, comprador):
        query = "INSERT INTO comprador (idComprador,cpf,telefoneComprador,nomeComprador,cid) VALUES(%s,%s,%s,%s,%s)"
        val = (comprador.idComprador,comprador.cpf,comprador.telefoneComprador,comprador.nomeComprador,comprador.cid) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()
    
    def encontraComprador(self, idComprador):
        self.criadb.instanciaDB(
            "SELECT * FROM comprador WHERE idComprador = %(id)s", {'id': idComprador},False)
        dicionario = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
        comprador = namedtuple('comprador', dicionario.keys())(*dicionario.values())
        return comprador
    
    def atualizaComprador(self,idComprador,cpf,telefoneComprador,nomeComprador,cid):
        val = (cpf,telefoneComprador,nomeComprador,cid,idComprador)
        self.criadb.instanciaDB("UPDATE comprador SET crm = %s, telefoneComprador = %s, nomeComprador = %s, cid = %s WHERE idComprador = %s",val,True)
        self.criadb.fechaDB()

    def deletaComprador(self,idComprador):
        self.criadb.instanciaDB("DELETE FROM comprador WHERE idComprador = %(id)s", {'id': idComprador},True)
        self.criadb.fechaDB()
    
    def retornaCompradores(self):
        self.criadb.instanciaDB(
            "SELECT * FROM comprador",None,False
        )
        dicionario = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        compradors = []
        i = 0
        while i<len(dicionario):
            comprador = namedtuple('comprador', dicionario[i].keys())(*dicionario[i].values())
            compradors.append(comprador)
            i = i + 1 
        
        return compradors