from database.conexao import Conexao

class Login():
    @staticmethod
    def login_usuario(nome, senha):
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", [nome, senha])
        usuario = cursor.fetchone() # pega o usuário encontrado
        conexao.close()
        return usuario 