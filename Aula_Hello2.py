from flask import Flask

app = Flask(__name__)

@app.route("/") # Rota raiz da aplicação no http
def index():
    return "Index"

@app.route("/hello") # Outra rota quando digitar "hello" no http
def hello():
    return "Hello World"

@app.route("/members") # Outra rota quando digitar "members" no http
def members():
    return "Members"

@app.route("/members/<string:name>/") # Outra rota quando digitar um nome qualquer depois de "members" no http
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()
