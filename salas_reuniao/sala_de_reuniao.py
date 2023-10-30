class SalaDeReuniao:
    def __init__(self, nome, horarios_disponiveis):
        self.nome = nome
        self.horarios_disponiveis = horarios_disponiveis
        self.reunioes_agendadas = []

    def agendar_reuniao(self, reuniao):
        if self.horarios_disponiveis[0] <= reuniao.inicio:
            self.horarios_disponiveis[0] = reuniao.fim
            self.reunioes_agendadas.append(reuniao)

    def __str__(self):
        return f"Sala de reunião '{self.nome}' disponível das {self.horarios_disponiveis[0]}h às {self.horarios_disponiveis[1]}h"

    def listar_reunioes_agendadas(self):
        if not self.reunioes_agendadas:
            return "Nenhuma reunião agendada nesta sala."
        else:
            reunioes = "\n".join([str(reuniao) for reuniao in self.reunioes_agendadas])
            return f"Reuniões agendadas nesta sala:\n{reunioes}"
