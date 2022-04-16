from platform import node
import mysql.connector

class CriaDB():
    mydb = None
    cursordb = None
    host = ""
    usuario = ""
    senha = ""
    base = ""

    def __init__(self, host , usuario,  senha, base):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.base = base

    def instanciaDB(self, query,val,comita):

        self.mydb = mysql.connector.connect(
            host = self.host,
            user = self.usuario,
            passwd = self.senha,
            database = self.base,
        )

        self.cursordb = self.mydb.cursor(dictionary=True)

        self.cursordb.execute(
            "CREATE DATABASE IF NOT EXISTS pi2_db"
        )

        self.cursordb.execute(query,val)
        
        if comita == True:
            self.mydb.commit()

    def fechaDB(self):
        self.cursordb.close()
            
        self.mydb.close()