class No:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.anterior = None
        self.proximo = None


class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_comum(self, nome):
        novo = No(nome, "Comum")

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def adicionar_preferencial(self, nome):
        novo = No(nome, "Preferencial")

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def atender(self):
        if self.inicio is None:
            print("Não há clientes na fila.")
            return

        cliente = self.inicio

        print("\nCliente atendido:", cliente.nome)
        print("Tipo:", cliente.tipo)

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

    def listar(self):
        if self.inicio is None:
            print("\nA fila está vazia.")
            return

        aux = self.inicio
        posicao = 1

        print("\nORDEM ATUAL DE ATENDIMENTO:")

        while aux is not None:
            print(
                posicao, "-",
                aux.nome,
                "| Tipo:", aux.tipo
            )

            aux = aux.proximo
            posicao += 1


def main():
    fila = Deque()

    while True:
        print("1 - Adicionar cliente comum")
        print("2 - Adicionar cliente preferencial")
        print("3 - Atender próximo cliente")
        print("4 - Mostrar fila")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente comum: ")
            fila.adicionar_comum(nome)
            fila.listar()

        elif opcao == "2":
            nome = input("Nome do cliente preferencial: ")
            fila.adicionar_preferencial(nome)
            fila.listar()

        elif opcao == "3":
            fila.atender()
            fila.listar()

        elif opcao == "4":
            fila.listar()

        elif opcao == "5":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
