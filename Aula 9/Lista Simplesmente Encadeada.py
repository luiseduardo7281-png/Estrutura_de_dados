class No:
    def __init__(self, nome, gols=0):
        self.nome = nome
        self.gols = gols
        self.prox = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, nome, gols=0):
        novo = No(nome, gols)
        novo.prox = self.inicio
        self.inicio = novo

    def adicionar_final(self, nome, gols=0):
        novo = No(nome, gols)

        if self.inicio is None:
            self.inicio = novo
            return

        aux = self.inicio

        while aux.prox is not None:
            aux = aux.prox

        aux.prox = novo

    def percorrer(self):
        aux = self.inicio

        while aux is not None:
            print("Nome:", aux.nome, "| Gols:", aux.gols)
            aux = aux.prox

    def media_gols(self):
        if self.inicio is None:
            return 0

        soma = 0
        quantidade = 0

        aux = self.inicio

        while aux is not None:
            soma += aux.gols
            quantidade += 1
            aux = aux.prox

        return soma / quantidade


lista = ListaEncadeada()

lista.adicionar_inicio("Neymar", 3)
lista.adicionar_inicio("Vini Jr.", 5)

lista.adicionar_final("Rodrygo", 4)
lista.adicionar_final("Raphinha", 2)

print("JOGADORES:")
lista.percorrer()

print("\nMédia de gols:", lista.media_gols())
