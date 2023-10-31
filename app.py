from flask import Flask, render_template, request
from salas_reuniao.sala_de_reuniao import SalaDeReuniao
from reunioes.reuniao import Reuniao

app = Flask(__name__)

salas = []

def criar_sala(nome_sala, capacidade, horarios_disponiveis):
    nova_sala = SalaDeReuniao(nome_sala, horarios_disponiveis, capacidade)
    salas.append(nova_sala)

def agendar_reuniao(nova_reuniao):
    for sala in salas:
        if sala.horarios_disponiveis[0] <= nova_reuniao.inicio <= sala.horarios_disponiveis[1]:
            if not any(reuniao.inicio <= nova_reuniao.inicio <= reuniao.fim for reuniao in sala.reunioes_agendadas):
                sala.agendar_reuniao(nova_reuniao)
                return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_reuniao = request.form["nome_reuniao"]
        inicio_reuniao = int(request.form["inicio"])
        fim_reuniao = int(request.form["fim"])
        data_reuniao = request.form["data"]

        nova_reuniao = Reuniao(nome_reuniao, inicio_reuniao, fim_reuniao, data_reuniao)

        if not agendar_reuniao(nova_reuniao):
            nome_sala = f"Sala {len(salas) + 1}"
            capacidade = 10
            horarios_disponiveis = [8, 17]
            criar_sala(nome_sala, capacidade, horarios_disponiveis)
            agendar_reuniao(nova_reuniao)

    return render_template("index.html", salas=salas)

if __name__ == "__main__":
    app.run(debug=True)
