class No:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.status = False
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, id, nome):
        novo = No(id, nome)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def remover(self, id):
        if self.inicio is None:
            print("Lista vazia.")
            return

        aux = self.inicio

        while aux is not None:

            if aux.id == id:

                if aux == self.inicio:
                    self.inicio = aux.proximo

                    if self.inicio is not None:
                        self.inicio.anterior = None
                    else:
                        self.fim = None

                    return

                if aux == self.fim:
                    self.fim = aux.anterior
                    self.fim.proximo = None
                    return

                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior

                return

            aux = aux.proximo

        print("Servidor não encontrado.")

    def ligar(self, id):
        aux = self.inicio

        while aux is not None:
            if aux.id == id:
                aux.status = True
                print("Servidor ligado.")
                return

            aux = aux.proximo

        print("Servidor não encontrado.")

    def desligar(self, id):
        aux = self.inicio

        while aux is not None:
            if aux.id == id:
                aux.status = False
                print("Servidor desligado.")
                return

            aux = aux.proximo

        print("Servidor não encontrado.")

    def listar_frente(self):
        if self.inicio is None:
            print("Lista vazia.")
            return

        aux = self.inicio

        while aux is not None:
            if aux.status:
                status = "Ligado"
            else:
                status = "Desligado"

            print(
                "ID:", aux.id,
                "| Nome:", aux.nome,
                "| Status:", status
            )

            aux = aux.proximo

    def listar_tras(self):
        if self.fim is None:
            print("Lista vazia.")
            return

        aux = self.fim

        while aux is not None:
            if aux.status:
                status = "Ligado"
            else:
                status = "Desligado"

            print(
                "ID:", aux.id,
                "| Nome:", aux.nome,
                "| Status:", status
            )

            aux = aux.anterior

lista = ListaDuplamenteEncadeada()

lista.inserir(1, "Servidor Web")
lista.inserir(2, "Servidor Banco de Dados")
lista.inserir(3, "Servidor API")
lista.inserir(4, "Servidor Backup")

lista.ligar(1)
lista.ligar(3)

print("\nSERVIDORES - FRENTE:")
lista.listar_frente()

print("\nSERVIDORES - TRÁS:")
lista.listar_tras()

print("\nDesligando servidor 3...")
lista.desligar(3)

print("\nSERVIDORES APÓS DESLIGAR:")
lista.listar_frente()

print("\nRemovendo servidor 2...")
lista.remover(2)

print("\nSERVIDORES APÓS REMOÇÃO - FRENTE:")
lista.listar_frente()

print("\nSERVIDORES APÓS REMOÇÃO - TRÁS:")
lista.listar_tras()
