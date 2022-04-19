from collections import namedtuple
from db.criadb import CriaDB

class UsuarioDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB()

    def insereUsuario(self, usuario):
        query = "INSERT INTO usuario (login,senha,tipo) VALUES(%s,%s,%s)"
        val = (usuario.login,usuario.senha,usuario.tipo) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()
    
    def encontraUsuario(self, login):
        self.criadb.instanciaDB(
            "SELECT * FROM usuario WHERE login = %(login)s", {'login': login},False)
        dicionario = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
        usuario = namedtuple('usuario', dicionario.keys())(*dicionario.values())
        return usuario
    
    def atualizaUsuario(self,login,senha,tipo):
        val = (senha,tipo,login)
        self.criadb.instanciaDB("UPDATE usuario SET senha = %s, tipo = %s WHERE login = %s",val,True)
        self.criadb.fechaDB()

    def deletaUsuario(self,login):
        self.criadb.instanciaDB("DELETE FROM usuario WHERE login = %(login)s", {'login': login},True)
        self.criadb.fechaDB()
    
    def retornaUsuarios(self):
        self.criadb.instanciaDB(
            "SELECT * FROM usuario",None,False
        )
        dicionario = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        usuarios = []
        i = 0
        while i<len(dicionario):
            usuario = namedtuple('usuario', dicionario[i].keys())(*dicionario[i].values())
            usuarios.append(usuario)
            i = i + 1 
        
        return usuarios