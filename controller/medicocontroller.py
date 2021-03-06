from db.medicodb import MedicoDB
from model.medico import Medico


class MedicoController:
    def cadastrarMedico(self,crm,telefoneMedico,nomeMedico):
        todos = self.listarMedico()
        if len(todos) == 0:
            idMedico = 0
        else:
            ultimo = todos.pop()
            idMedico = int(ultimo.idMedico) + 1
        medico = Medico(idMedico,crm,telefoneMedico,nomeMedico)
        
        db = MedicoDB()
        db.insereMedico(medico)

        return medico

    def editarMedico(idMedico,crm,telefoneMedico,nomeMedico):
        db = MedicoDB()        
        db.atualizaMedico(idMedico,crm,telefoneMedico,nomeMedico)
        medico = Medico(idMedico,crm,telefoneMedico,nomeMedico)
        return medico

    def excluirMedico(idMedico):
        db = MedicoDB()
        db.deletaMedico(idMedico)

    def mostrarMedico(idMedico):
        db = MedicoDB()
        medico = db.encontraMedico(idMedico)
               
        return medico

    def listarMedico(self):
        db = MedicoDB()
        medicos = db.retornaMedicos()
        return medicos
