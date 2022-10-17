from flask import Flask, render_template
import plotly.graph_objects as go

app = Flask(__name__)

# criar a primeira pagina do site
# route -> link do site
# função para exibir algo na pagina

nomes = ['P.Duarte', 'Henrique', 'P.Alexandria', 'P.Elssie']
meta = 264
'''

fig = go.Figure(data=[
    go.line(name='Meta', x=nomes, y=[264, 264, 264, 264]),
    go.Bar(name='Alcançado', x=nomes, y=[240, 230, 215, 210]),
    go.Bar(name='Dias Fora', x=nomes, y=[8, 3, 0, 5]),
    #go.Bar(name='Concluido')
])
# Change the bar mode
fig.update_layout(barmode='group')

grafic = fig.show()
'''



@app.route('/')
def home():
    return render_template("home.html")

@app.route("/mesa<id_mesa>")
def mesa(id_mesa):
    return render_template("mesa.html", id_mesa=id_mesa)


@app.route("/grafic")
def grafic(grafic):
    return render_template("grafic.html", grafic=grafic)



# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

