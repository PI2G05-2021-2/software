class PerfilExtracao:
    idPerfil: int
    temperatura: float
    tempo: int
    potencia: float
    velocidade: float


    def __init__(self, idPerfil: int, temperatura: float, tempo: int, potencia: float, velocidade: float):
        self.idPerfil = idPerfil
        self.temperatura = temperatura
        self.tempo = tempo
        self.potencia = potencia
        self.velocidade = velocidade