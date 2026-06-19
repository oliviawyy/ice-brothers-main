from flask import Flask, render_template, session, redirect, request, jsonify
from model.login import Login
from model.produtos import recuperar_produto_por_codigo
from database.conexao import Conexao

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

@app.route('/produto')
def pag_produto():
    produto_procurado = recuperar_produto_por_codigo(1)  
   
    return render_template("pagina_produto.html", produto=produto_procurado)

@app.route('/carrinho')
def ver_carrinho():
    carrinho_sessao = session.get('carrinho', []) 
# pegou a lista e salva na sessao
    subtotal = 0
    itens_carrinho = []
    
    for item in carrinho_sessao:
        produto = recuperar_produto_por_codigo(item['codigo'])
        
        if produto:
            produto_completo = {
                'codigo': produto[0],
                'nome': produto[1],
                'valor': float(produto[3]),
                'foto': produto[4],
                'tamanho': item['tamanho'],
                'quantidade': item['quantidade']
            }
            subtotal += produto_completo['valor'] * produto_completo['quantidade']
            itens_carrinho.append(produto_completo)
    return render_template('carrinho.html', itens_carrinho=itens_carrinho, subtotal=subtotal)

if __name__ == '__main__':
     app.run(debug=True)
