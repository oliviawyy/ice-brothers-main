from flask import Flask, render_template, session, redirect, request, jsonify

app = Flask(__name__)
app.secret_key = "ice_brothers"


@app.route("/")
def pagina_principal():
     return render_template("index.html")

