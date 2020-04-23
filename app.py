from flask import Flask, render_template, request
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

app.run(debug=True)
#port=os.environ["PORT"]
#app.run('0.0.0.0', int(port), debug=False)