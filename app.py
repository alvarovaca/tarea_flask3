from flask import Flask, render_template, request, abort
import json
#import os
app = Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET"])
def juegos():
    return render_template("juegos.html")

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
    nombre=request.form.get("name")
    for i in datos:
        if nombre == "" or str(i["nombre"]).startswith(nombre) :
            return render_template('listajuegos.html',juegos=datos,nombre=nombre)
    return render_template('listajuegos.html')

@app.route('/juego/<int:identificador>',methods=["GET"])
def juego(identificador):
    for i in datos:
        if i["id"] == identificador:
            return render_template('juego.html',juego=i)
    abort(404)

app.run(debug=True)
#port=os.environ["PORT"]
#app.run('0.0.0.0', int(port), debug=False)