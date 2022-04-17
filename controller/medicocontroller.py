from db.medicodb import MedicoDB
from model.medico import Medico


class MedicoController:
    def cadastrarMedico(idMedico,crm,telefoneMedico,nomeMedico):
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

    def listarMedico():
        db = MedicoDB()
        medicos = db.retornaMedicos()
        return medicos
