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



if __name__ == '__main__':
     app.run(debug=True)
