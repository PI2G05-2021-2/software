from collections import namedtuple
from db.criadb import CriaDB

class PerfilExtracaoDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB()

    def inserePerfilExtracao(self,perfil):
        query = "INSERT INTO perfilExtracao (idPerfil, temperatura, tempo, potencia, velocidade) VALUES(%s,%s,%s,%s,%s)"
        val = (perfil.idPerfil,perfil.temperatura, perfil.tempo, perfil.potencia, perfil.velocidade) 
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
    
    def retornaPerfis(self):
        self.criadb.instanciaDB(
            "SELECT * FROM perfilextracao",None,False
        )
        dicionario = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        perfis = []
        i = 0
        while i<len(dicionario):
            perfil = namedtuple('perfil', dicionario[i].keys())(*dicionario[i].values())
            perfis.append(perfil)
            i = i + 1 
        
        return perfis