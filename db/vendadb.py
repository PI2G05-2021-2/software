from collections import namedtuple
from db.compradordb import CompradorDB
from db.criadb import CriaDB
from db.lotedb import LoteDB
from db.medicodb import MedicoDB
from db.usuariodb import UsuarioDB
from model.venda import Venda
# import win32api

class VendaDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB()        

    def insereVenda(self, venda):
        query = "INSERT INTO venda (idVenda,fk_medico_idMedico,fk_comprador_idComprador,endereco,fk_Usuario_login,fk_Lote_idLote) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (venda.idVenda,venda.medico.idMedico,venda.comprador.idComprador, venda.endereco,venda.usuario.login,venda.lote.idLote) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()
    
    def encontraVenda(self, idVenda):
        self.criadb.instanciaDB(
            "SELECT * FROM venda WHERE idVenda = %(id)s", {'id': idVenda},False)
        dicionario = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
        vendatemp = namedtuple('vendatemp', dicionario.keys())(*dicionario.values())
        venda = Venda(vendatemp.idVenda,MedicoDB.encontraMedico(vendatemp.fk_medico_idMedico),CompradorDB.encontraComprador(vendatemp.fk_comprador_idComprador),
                    vendatemp.endereco,UsuarioDB.encontraUsuario(vendatemp.fk_Usuario_login), LoteDB.encontraLote(vendatemp.fk_Lote_idLote))
        return venda
    
    def atualizaVenda(self,idVenda, medico, comprador, endereco, usuario, lote):
        query = "UPDATE venda SET fk_medico_idMedico = %s, fk_comprador_idComprador = %s, endereco = %s, fk_Usuario_login = %s, fk_Lote_idLote = %s WHERE idVenda = %s"
        val = (medico.idMedico,comprador.idComprador,endereco, usuario.login,lote.idLote,idVenda)
        self.criadb.instanciaDB(query,val,True)
        self.criadb.fechaDB()

    def deletaVenda(self,idVenda):
        self.criadb.instanciaDB("DELETE FROM venda WHERE idVenda = %(id)s", {'id': idVenda},True)
        self.criadb.fechaDB()
    
    def retornaVendas(self):
        self.criadb.instanciaDB(
            "SELECT * FROM venda",None,False
        )
        dicionario = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        vendas = []
        i = 0
        while i<len(dicionario):
            # win32api.MessageBox(0, str(dicionario[i]), 'title')
            vendatemp = namedtuple('vendatemp', dicionario[i].keys())(*dicionario[i].values())
            medico = MedicoDB().encontraMedico(vendatemp.fk_medico_idMedico)
            comprador = CompradorDB().encontraComprador(vendatemp.fk_comprador_idComprador)
            usuario = UsuarioDB().encontraUsuario(vendatemp.fk_Usuario_login3)
            lote = LoteDB().encontraLote(vendatemp.fk_Lote_idLote)

            venda = Venda(vendatemp.idVenda,medico,comprador,vendatemp.endereco,usuario,lote)
            vendas.append(venda)
            i = i + 1 
        
        return vendas