from db.criadb import CriaDB

class UsuarioDB:
    criadb = None

    def __init__(self) :
        self.criadb = CriaDB("localhost","pi2","P.assword123","pi2_db")
        self.criaTabela()

    def criaTabela(self):
        self.criadb.instanciaDB(
            """CREATE TABLE IF NOT EXISTS Usuario (
                login char(15) PRIMARY KEY,
                senha char(15),
                tipo char(1)
            );""", None,True
        )
        self.criadb.fechaDB()
        

    def insereUsuario(self, usuario):
        query = "INSERT INTO usuario (login,senha,tipo) VALUES(%s,%s,%s)"
        val = (usuario.login,usuario.senha,usuario.tipo) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()
    
    def encontraUsuario(self, login):
        self.criadb.instanciaDB(
            "SELECT * FROM usuario WHERE login = %(login)s", {'login': login},False)
        usuario = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
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
        usuarios = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        return usuarios