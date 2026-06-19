from database.conexao import Conexao

class Login():
    @staticmethod
    def login_usuario(nome, senha):
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", [nome, senha])
<<<<<<< HEAD
        usuario = cursor.fetchone() # pega o usuário encontrado
        conexao.close()
        return usuario 
=======
        resultado = cursor.fetchall()
        conexao.commit()
        conexao.close()
        return resultado
>>>>>>> 8e6da39f76484789e18f7a96744df4f590e4a87c
