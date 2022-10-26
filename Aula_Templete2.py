from flask import Flask, flash, redirect, render_template, request, session, abort

# Criando o objeto app
app = Flask(__name__)

# Colocando a mensagem inicial 
@app.route("/")
def index():
    return "Flask App!"

# Colocando a mensagem com o template html na rota digitada
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template("template2.html", name=name)

# Executando o app na porta 80
if __name__=="__main__": 
    app.run(host="0.0.0.0", port=80)