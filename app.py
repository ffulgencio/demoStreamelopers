from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask import json, jsonify

app = Flask(__name__)

todos = []

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        if request.form['todo'] != '':
            todos.append(request.form['todo']);
    return render_template("todo.html", todos=todos)

@app.route("/borrar/<todo>")
def borrar(todo):
    todos.remove(todo)
    return redirect(url_for('index'))


@app.route("/login/<user>")
def login(user):
    return user

@app.route("/jsonfile")
def get_json():
    return jsonify(nombre="Jhon", lastName="Snow")

app.run(debug=True)
