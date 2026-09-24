class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        novo = NoDuploCircular(dado)

        if self.inicio is None:
            novo.proximo = novo
            novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior

            novo.proximo = self.inicio
            novo.anterior = ultimo

            ultimo.proximo = novo
            self.inicio.anterior = novo

            self.inicio = novo

    def adicionar_final(self, dado):
        novo = NoDuploCircular(dado)

        if self.inicio is None:
            novo.proximo = novo
            novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior

            novo.proximo = self.inicio
            novo.anterior = ultimo

            ultimo.proximo = novo
            self.inicio.anterior = novo

    def percorrer_frente(self, quantidade):
        if self.inicio is None:
            print("Lista vazia.")
            return

        aux = self.inicio

        for i in range(quantidade):
            print(aux.dado)
            aux = aux.proximo

    def percorrer_tras(self, quantidade):
        if self.inicio is None:
            print("Lista vazia.")
            return

        aux = self.inicio.anterior

        for i in range(quantidade):
            print(aux.dado)
            aux = aux.anterior

    def remover(self, dado):
        if self.inicio is None:
            return

        aux = self.inicio

        while True:

            if aux.dado == dado:

                if aux.proximo == aux:
                    self.inicio = None
                    return

                if aux == self.inicio:
                    ultimo = self.inicio.anterior
                    novo_inicio = self.inicio.proximo

                    ultimo.proximo = novo_inicio
                    novo_inicio.anterior = ultimo

                    self.inicio = novo_inicio
                    return

                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior

                return

            aux = aux.proximo

            if aux == self.inicio:
                break

lista = ListaDuplamenteEncadeadaCircular()

lista.adicionar_inicio("Jogador 1")
lista.adicionar_inicio("Jogador 2")
lista.adicionar_inicio("Jogador 3")

lista.adicionar_final("Jogador 4")
lista.adicionar_final("Jogador 5")

print("PERCORRENDO PARA FRENTE:")
lista.percorrer_frente(7)

print("\nPERCORRENDO PARA TRÁS:")
lista.percorrer_tras(7)

print("\nRemovendo Jogador 3...")
lista.remover("Jogador 3")

print("\nLISTA APÓS REMOÇÃO - FRENTE:")
lista.percorrer_frente(6)

print("\nLISTA APÓS REMOÇÃO - TRÁS:")
lista.percorrer_tras(6)
