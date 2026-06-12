import mysql.connector 

class Conexao():
    def conectar():
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="root",
            database="ice_brothers"
        )
        cursor = conexao.cursor(dictionary=True)
        return conexao, cursor