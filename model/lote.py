from model.perfilExtrcao import PerfilExtracao
from model.usuario import Usuario

class Lote:
    usuario: Usuario
    perfil: PerfilExtracao
    idLote: int

    def __init__(self, idLote: int, perfil: PerfilExtracao, usuario: Usuario):
        self.idLote = idLote
        self.perfil = perfil
        self.usuario = usuario
    