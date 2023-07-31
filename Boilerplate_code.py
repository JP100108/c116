from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    INP = "joao"
    return render_template("T.html", Uname=INP)

@app.route("/treinamento", methods=["POST"])
def treinamento():
    treino = request.form["treino"]
    return f"<h1>Treino enviado: {treino}</h1>"

if __name__ == "__main__":
    app.run()
