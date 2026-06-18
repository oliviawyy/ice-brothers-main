from flask import Flask, render_template, session, redirect, request, jsonify
from model.login import Login

app = Flask(__name__)
app.secret_key = "ice_brothers"


@app.route("/")
def pagina_principal():
     return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logar", methods=["POST", "GET"])
def pag_logar():
     usuario = request.form.get("usuario")
     senha = request.form.get("senha") 

     usuario_logado = Login.login_usuario(usuario, senha)


     if usuario_logado:
          return redirect("/")
     else:
          return render_template("login.html")

@app.route("/cadastro")
def pag_cadastro():
     return render_template("cadastro.html")

@app.route("/produto")
def pag_produto():
     return render_template("pagina_produto.html")

@app.route('/carrinho')
def ver_carrinho():
    carrinho_sessao = session.get('carrinho', []) 
    
    subtotal = 0
    itens_carrinho = []
    
    
    cursor = mysql.connection.cursor()
    for item in carrinho_sessao:
        cursor.execute("SELECT * FROM produtos WHERE codigo = %s", [item['codigo']])
        produto = cursor.fetchone() # Retorna um dicionário ou tupla do banco
        
        if produto:
            # Junta as infos do banco com a quantidade e tamanho escolhidos
            produto_completo = {
                'codigo': produto['codigo'],
                'nome': produto['nome'],
                'foto': produto['foto'],
                'valor': float(produto['valor']),
                'tamanho': item['tamanho'],
                'quantidade': item['quantidade']
            }
            subtotal += produto_completo['valor'] * produto_completo['quantidade']
            itens_carrinho.append(produto_completo)
            
    cursor.close()
    
    # Renderiza passando os dados para o Jinja2 trabalhar
    return render_template('carrinho.html', itens_carrinho=itens_carrinho, subtotal=subtotal)

if __name__ == '__main__':
     app.run(debug=True)
