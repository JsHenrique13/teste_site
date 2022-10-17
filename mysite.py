from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira pagina do site
# route -> link do site
# função para exibir algo na pagina


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/mesa/<id_mesa>")
def mesa(id_mesa):
    return render_template("mesa.html", id_mesa=id_mesa)



# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

