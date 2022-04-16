from db.usuariodb import UsuarioDB
from model.usuario import Usuario


class UsuarioController:
    def cadastrarUsuario(login,senha,tipo):
        usuario = Usuario(login,senha,tipo)
        
        db = UsuarioDB()
        db.insereUsuario(usuario)

        return usuario

    def editarUsuario(login,senha,tipo):
        db = UsuarioDB()        
        db.atualizaUsuario(login,senha,tipo)
        usuario = Usuario(login,senha,tipo)
        return usuario

    def excluirUsuario(login):
        db = UsuarioDB()
        db.deletaUsuario(login)

    def mostrarUsuario(login):
        db = UsuarioDB()
        usuario = db.encontraUsuario(login)
               
        return usuario

    def listarUsuario():
        db = UsuarioDB()
        usuarios = db.retornaUsuarios()
        return usuarios
