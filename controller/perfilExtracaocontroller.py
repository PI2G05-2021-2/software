from db.perfilExtracaodb import PerfilExtracaoDB
from model.perfilExtrcao import PerfilExtracao


class PerfilExtracaoController:

    def cadastrarPerfilExtracao(temperatura: float, tempo: int, potencia: float, velocidade: float):
        db = PerfilExtracaoDB()
        lista = db.retornaPerfis()
        if len(lista) == 0:
            idPerfil = 0
        else:
            ultimo = lista.pop()
            idPerfil = int(ultimo.idPerfil) + 1
        perfil = PerfilExtracao(idPerfil,temperatura,tempo, potencia,velocidade)
        db.inserePerfilExtracao(perfil)

        return perfil

    def mostrarPerfilExtracao(self,idPerfil):
        db = PerfilExtracaoDB()
        
        perfil = db.encontraPerfilExtracao(idPerfil)
        #perfil = PerfilExtracao(lista[0],float(lista[1]),lista[2],float(lista[3]),float(lista[4]))
        
        return perfil
    
    def listarPerfis():
        db = PerfilExtracaoDB()
        perfis = db.retornaPerfis()
        return perfis

