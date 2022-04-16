from collections import namedtuple
from db.criadb import CriaDB

class PerfilExtracaoDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB("localhost","pi2","P.assword123","pi2_db")
        self.criaTabela()

    def criaTabela(self):
        self.criadb.instanciaDB(
            """CREATE TABLE IF NOT EXISTS PerfilExtracao (
                idPerfil int(5) NOT NULL AUTO_INCREMENT,
                temperatura double,
                tempo int,
                potencia double,
                velocidade double,
                PRIMARY KEY (`idPerfil`)
            )ENGINE=InnoDB AUTO_INCREMENT=10000;""", None,True
        )
        self.criadb.fechaDB()

    def inserePerfilExtracao(self,perfil):
        query = "INSERT INTO perfilExtracao (temperatura, tempo, potencia, velocidade) VALUES(%s,%s,%s,%s)"
        val = (perfil.temperatura, perfil.tempo, perfil.potencia, perfil.velocidade) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()

    def localizaIdPerfil(self,temperatura: float, tempo: int, potencia: float, velocidade: float):
        query = "SELECT * FROM perfilextracao WHERE (temperatura = %s AND tempo = %s AND potencia = %s AND velocidade = %s)"
        val = (temperatura,tempo,potencia,velocidade)
        self.criadb.instanciaDB(query,val,False)
        
        perfil = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()  
        perfilExtracao = namedtuple('perfilExtracao', perfil.keys())(*perfil.values())
        
        return perfilExtracao

    def encontraPerfilExtracao(self, idPerfil):
        self.criadb.instanciaDB(
            "SELECT * FROM perfilextracao WHERE idPerfil = %(id)s", {'id': idPerfil},False)
        
        perfil = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
        perfilExtracao = namedtuple('perfilExtracao', perfil.keys())(*perfil.values())

        return perfilExtracao