import tkinter as tk
from salas_reuniao.sala_de_reuniao import SalaDeReuniao
from reunioes.reuniao import Reuniao

def agendar_reuniao():
    nome_reuniao = entry_nome_reuniao.get()
    inicio_reuniao = int(entry_inicio.get())
    fim_reuniao = int(entry_fim.get())

    nova_reuniao = Reuniao(nome_reuniao, inicio_reuniao, fim_reuniao)

    for sala in salas:
        if sala.horarios_disponiveis[0] <= nova_reuniao.inicio:
            sala.agendar_reuniao(nova_reuniao)
            break

    update_display()

def update_display():
    display_salas.config(state=tk.NORMAL)
    display_salas.delete(1.0, tk.END)
    for sala in salas:
        display_salas.insert(tk.END, f"{sala.nome}: {sala.listar_reunioes_agendadas()}\n")
    display_salas.config(state=tk.DISABLED)

salas = []
for i in range(1, 11):
    nome_sala = f"Sala {i}"
    horarios_disponiveis = [8, 17]
    sala = SalaDeReuniao(nome_sala, horarios_disponiveis)
    salas.append(sala)

root = tk.Tk()
root.title("Agendamento de Reuniões")

label_nome_reuniao = tk.Label(root, text="Nome da Reunião:")
entry_nome_reuniao = tk.Entry(root)
label_inicio = tk.Label(root, text="Horário de Início (hh):")
entry_inicio = tk.Entry(root)
label_fim = tk.Label(root, text="Horário de Término (hh):")
entry_fim = tk.Entry(root)
btn_agendar = tk.Button(root, text="Agendar Reunião", command=agendar_reuniao)
display_salas = tk.Text(root, height=10, width=50)
display_salas.config(state=tk.DISABLED)

label_nome_reuniao.grid(row=0, column=0)
entry_nome_reuniao.grid(row=0, column=1)
label_inicio.grid(row=1, column=0)
entry_inicio.grid(row=1, column=1)
label_fim.grid(row=2, column=0)
entry_fim.grid(row=2, column=1)
btn_agendar.grid(row=3, column=0, columnspan=2)
display_salas.grid(row=4, column=0, columnspan=2)

update_display()

root.mainloop()
