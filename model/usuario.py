class Usuario:
    login = ""
    senha = ""
    tipo = ""

    def __init__(self,login,senha,tipo) :
        self.login = login
        self.senha = senha
        self.tipo = tipo