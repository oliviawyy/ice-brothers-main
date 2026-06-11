from flask import Flask, render_template, session, redirect, request, jsonify

app = Flask(__name__)
app.secret_key = "ice_brothers"


@app.route("/")
def pagina_principal():
     return render_template("index.html")

@app.route("/logar")
def pag_logar():
     return render_template("login.html")

if __name__ == '__main__':
     app.run(debug=True)