class Usuario:
    login: str
    senha: str
    tipo: str

    def __init__(self,login: str,senha: str,tipo: str) :
        self.login = login
        self.senha = senha
        self.tipo = tipo