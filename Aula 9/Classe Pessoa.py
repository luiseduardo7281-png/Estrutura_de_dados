class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)


pessoa1 = Pessoa("João", 20)
pessoa2 = Pessoa("Maria", 25)

pessoa1.apresentar()

print()

pessoa2.apresentar()
