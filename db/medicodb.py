from collections import namedtuple
from db.criadb import CriaDB

class MedicoDB:
    criadb: CriaDB

    def __init__(self) :
        self.criadb = CriaDB()

    def insereMedico(self, medico):
        query = "INSERT INTO medico (idMedico,crm,telefoneMedico,nomeMedico) VALUES(%s,%s,%s,%s)"
        val = (medico.idMedico,medico.crm,medico.telefoneMedico,medico.nomeMedico) 
        self.criadb.instanciaDB(query, val, True)
        self.criadb.fechaDB()
    
    def encontraMedico(self, idMedico):
        self.criadb.instanciaDB(
            "SELECT * FROM medico WHERE idMedico = %(id)s", {'id': idMedico},False)
        dicionario = self.criadb.cursordb.fetchone()
        self.criadb.fechaDB()
        medico = namedtuple('medico', dicionario.keys())(*dicionario.values())
        return medico
    
    def atualizaMedico(self,idMedico,crm,telefoneMedico,nomeMedico):
        val = (crm,telefoneMedico,nomeMedico,idMedico)
        self.criadb.instanciaDB("UPDATE medico SET crm = %s, telefoneMedico = %s, nomeMedico = %s WHERE idMedico = %s",val,True)
        self.criadb.fechaDB()

    def deletaMedico(self,idMedico):
        self.criadb.instanciaDB("DELETE FROM medico WHERE idMedico = %(id)s", {'id': idMedico},True)
        self.criadb.fechaDB()
    
    def retornaMedicos(self):
        self.criadb.instanciaDB(
            "SELECT * FROM medico",None,False
        )
        dicionario = self.criadb.cursordb.fetchall()
        self.criadb.fechaDB()
        medicos = []
        i = 0
        while i<len(dicionario):
            medico = namedtuple('medico', dicionario[i].keys())(*dicionario[i].values())
            medicos.append(medico)
            i = i + 1 
        
        return medicos