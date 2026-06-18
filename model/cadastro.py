from database.conexao import Conexao

class Cadastro():
    def cadastrar_usuario(nome, email, endereco, CEP, senha):
        conexao, cursor = Conexao.conectar()
        cursor.execute("INSERT INTO usuarios (nome, email, endereco, CEP, senha) VALUES (%s, %s, %s, %s, %s)", [nome, email, endereco, CEP, senha])
        conexao.commit()
        conexao.close()
        