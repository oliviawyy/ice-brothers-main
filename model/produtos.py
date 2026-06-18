from database.conexao import Conexao

def recuperar_produ():
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT * FROM produtos")
        produto = cursor.fetchone()
        conexao.close()
        return produto
        