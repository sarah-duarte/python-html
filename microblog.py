from flask import Flask

app = Flask("microblog")

#decorator - operador do python que fica em cima da função e ele faz alguma coisa com essa função. 
@app.route("/")
def index():
    return "Hello World"

app.run()