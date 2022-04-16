from db.perfilExtracaodb import PerfilExtracaoDB
from model.perfilExtrcao import PerfilExtracao


class PerfilExtracaoController:

    def cadastrarPerfilExtracao(temperatura: float, tempo: int, potencia: float, velocidade: float):
        perfil = PerfilExtracao(None,temperatura,tempo, potencia,velocidade)
        db = PerfilExtracaoDB()
        db.inserePerfilExtracao(perfil)
        lista = db.localizaIdPerfil(temperatura,tempo, potencia,velocidade)
        perfilCadastrado  = PerfilExtracao(int(lista[0]),float(lista[1]),int(lista[2]),float(lista[3]),float(lista[4]))

        return perfilCadastrado

    def mostrarPerfilExtracao(idPerfil):
        db = PerfilExtracaoDB()
        
        lista = db.encontraPerfilExtracao(idPerfil)
        perfil = PerfilExtracao(lista[0],float(lista[1]),lista[2],float(lista[3]),float(lista[4]))
        
        return perfil

