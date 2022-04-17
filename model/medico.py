class Medico:
    idMedico: int
    crm: str
    telefoneMedico: str
    nomeMedico: str

    def __init__(self, idMedico: int,crm: str,telefoneMedico: str,nomeMedico: str):
        self.idMedico = idMedico
        self.crm = crm
        self.telefoneMedico = telefoneMedico
        self.nomeMedico = nomeMedico