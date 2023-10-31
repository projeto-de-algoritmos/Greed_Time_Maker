class Reuniao:
    def __init__(self, nome, inicio, fim, data, sala=None):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.data = data
        self.sala = sala

    def __str__(self):
        return f"Reunião '{self.nome}' das {self.inicio}h às {self.fim}h"
