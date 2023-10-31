from flask import Flask, render_template, request
from salas_reuniao.sala_de_reuniao import SalaDeReuniao
from reunioes.reuniao import Reuniao

app = Flask(__name__)

salas = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_reuniao = request.form["nome_reuniao"]
        inicio_reuniao = int(request.form["inicio"])
        fim_reuniao = int(request.form["fim"])

        nova_reuniao = Reuniao(nome_reuniao, inicio_reuniao, fim_reuniao)

        for sala in salas:
            if sala.horarios_disponiveis[0] <= nova_reuniao.inicio:
                sala.agendar_reuniao(nova_reuniao)
                break

    return render_template("index.html", salas=salas)

if __name__ == "__main__":
    for i in range(1, 11):
        nome_sala = f"Sala {i}"
        horarios_disponiveis = [8, 17]
        sala = SalaDeReuniao(nome_sala, horarios_disponiveis)
        salas.append(sala)
    app.run(debug=True)
