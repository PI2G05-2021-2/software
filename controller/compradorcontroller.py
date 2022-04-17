from db.compradordb import CompradorDB
from model.comprador import Comprador


class CompradorController:
    def cadastrarComprador(idComprador,cpf,telefoneComprador,nomeComprador,cid):
        comprador = Comprador(idComprador,cpf,telefoneComprador,nomeComprador,cid)
        
        db = CompradorDB()
        db.insereComprador(comprador)

        return comprador

    def editarComprador(idComprador,cpf,telefoneComprador,nomeComprador,cid):
        db = CompradorDB()        
        db.atualizaComprador(idComprador,cpf,telefoneComprador,nomeComprador,cid)
        comprador = Comprador(idComprador,cpf,telefoneComprador,nomeComprador,cid)
        return comprador

    def excluirComprador(idComprador):
        db = CompradorDB()
        db.deletaComprador(idComprador)

    def mostrarComprador(idComprador):
        db = CompradorDB()
        comprador = db.encontraComprador(idComprador)
               
        return comprador

    def listarComprador():
        db = CompradorDB()
        compradores = db.retornaCompradores()
        return compradores
        
