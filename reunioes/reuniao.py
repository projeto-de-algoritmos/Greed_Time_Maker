class Reuniao:
    def __init__(self, nome, inicio, fim):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim

    def __str__(self):
        return f"Reunião '{self.nome}' das {self.inicio}h às {self.fim}h"
