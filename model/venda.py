from model.comprador import Comprador
from model.lote import Lote
from model.medico import Medico
from model.usuario import Usuario


class Venda:
    idVenda: int
    medico: Medico
    comprador: Comprador
    endereco: str
    usuario: Usuario
    lote: Lote

    def __init__(self,idVenda: int,medico: Medico,comprador: Comprador,endereco: str,usuario: Usuario,lote: Lote):
        self.idVenda = idVenda
        self.medico = medico
        self.comprador = comprador
        self.endereco = endereco
        self.usuario = usuario
        self.lote = lote