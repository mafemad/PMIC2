from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html", background= url_for('static', filename='imagens/fundo.png'))

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html", background= url_for('static', filename='imagens/fundo2.png'))

@app.route("/contato")
def contato():
    return render_template('contato.html', background= url_for('static', filename='imagens/fundo2.png'))

app.run(debug=True)