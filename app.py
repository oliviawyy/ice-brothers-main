from flask import Flask, render_template, session, redirect, request, jsonify

app = Flask(__name__)
app.secret_key = "ice_brothers"


@app.route("/")
def pagina_principal():
     return render_template("index.html")

@app.route("/logar")
def pag_logar():
     return render_template("login.html")

<<<<<<< HEAD
if __name__ == '__main__':
     app.run(debug=True)
=======


if __name__=="__main__":
    app.run(debug=True)
>>>>>>> 5d088e3defe0f7de96d84ecdb24c8dac81c99092
