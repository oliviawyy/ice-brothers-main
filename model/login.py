from database.conexao import Conexao

class Login():
    def  login_usuario(nome, senha):
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", [nome, senha])
        resultado = cursor.fetchall()
        conexao.commit()
        conexao.close()
        return resultado
