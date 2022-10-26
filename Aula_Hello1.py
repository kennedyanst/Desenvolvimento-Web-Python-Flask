from flask import Flask


# Criando a app
app = Flask(__name__) 

# Quero que a app fique no diretorio raiz
@app.route("/")

def hello():
    return "Hello, World"

# Executando a função
if __name__ == "__main__":
    app.run()