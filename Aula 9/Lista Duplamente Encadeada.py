class NoDuplo:
    def __init__(self, nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_inicio(self, nome):
        novo = NoDuplo(nome)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def percorrer_frente(self):
        aux = self.inicio

        while aux is not None:
            print(aux.nome)
            aux = aux.proximo

    def percorrer_tras(self):
        aux = self.fim

        while aux is not None:
            print(aux.nome)
            aux = aux.anterior

lista = ListaDuplamenteEncadeada()

lista.adicionar_inicio("Jogador 1")
lista.adicionar_inicio("Jogador 2")
lista.adicionar_inicio("Jogador 3")
lista.adicionar_inicio("Jogador 4")

print("ORDEM DA FRENTE PARA TRÁS:")
lista.percorrer_frente()

print("\nORDEM DE TRÁS PARA FRENTE:")
lista.percorrer_tras()
