from database.conexao import Conexao

def recuperar_produ():
    conexao, cursor = Conexao.conectar()
    cursor.execute("SELECT * FROM produtos")
    produto = cursor.fetchone()
    conexao.close()
    return produto


def recuperar_produto_por_codigo(codigo):
    conexao, cursor = Conexao.conectar()
    cursor.execute("SELECT * FROM produtos WHERE codigo = %s", (codigo,))
    produto = cursor.fetchone()
    conexao.close()
    return produto