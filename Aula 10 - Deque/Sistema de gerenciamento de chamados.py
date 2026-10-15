class No:
    def __init__(self, chamado):
        self.chamado = chamado
        self.anterior = None
        self.proximo = None

class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_fim(self, chamado):
        novo = No(chamado)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

    def adicionar_inicio(self, chamado):
        novo = No(chamado)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def atender_inicio(self):
        if self.inicio is None:
            print("Não há chamados para atender.")
            return

        chamado = self.inicio.chamado

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

        print("Chamado atendido:", chamado)

    def atender_fim(self):
        if self.fim is None:
            print("Não há chamados para atender.")
            return

        chamado = self.fim.chamado

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None

        print("Chamado atendido:", chamado)

    def listar(self):
        if self.inicio is None:
            print("A fila de chamados está vazia.")
            return

        aux = self.inicio

        print("\nFILA ATUAL:")

        while aux is not None:
            print("-", aux.chamado)
            aux = aux.proximo


def main():
    fila = Deque()

    while True:
        print("1 - Adicionar chamado no fim (comum)")
        print("2 - Adicionar chamado no início (urgente)")
        print("3 - Atender chamado do início")
        print("4 - Atender chamado do fim")
        print("5 - Listar todos os chamados")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            chamado = input("Descrição do chamado comum: ")
            fila.adicionar_fim(chamado)
            fila.listar()

        elif opcao == "2":
            chamado = input("Descrição do chamado urgente: ")
            fila.adicionar_inicio(chamado)
            fila.listar()

        elif opcao == "3":
            fila.atender_inicio()
            fila.listar()

        elif opcao == "4":
            fila.atender_fim()
            fila.listar()

        elif opcao == "5":
            fila.listar()

        elif opcao == "6":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")
