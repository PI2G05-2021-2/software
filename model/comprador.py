class Comprador:
    idComprador: int
    cpf: str
    telefoneComprador: str
    nomeComprador: str
    cid: str

    def __init__(self,idComprador: int,cpf: str,telefoneComprador: str,nomeComprador: str,cid: str):
        self.idComprador = idComprador
        self.cpf = cpf
        self.telefoneComprador = telefoneComprador
        self.nomeComprador = nomeComprador
        self.cid = cid