class Sala:
    def __init__(self, nome, capacidade, descricao):
        self.nome = nome
        self.capacidade = capacidade
        self.descricao = descricao

    def __str__(self):
        return f"Sala '{self.nome}': Capacidade para {self.capacidade} pessoas. {self.descricao}"

if __name__ == "__main__":
    sala1 = Sala("Sala 1", 10, "Sala de reunião executiva")
    sala2 = Sala("Sala 2", 6, "Sala de treinamento")

    print(sala1)
    print(sala2)
