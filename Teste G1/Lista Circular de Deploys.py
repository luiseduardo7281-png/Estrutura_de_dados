class No:
    def __init__(self, nome, duracao, ambiente):
        self.nome = nome
        self.duracao = duracao
        self.ambiente = ambiente
        self.ativo = False
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def adicionar(self, nome, duracao, ambiente):
        novo = No(nome, duracao, ambiente)

        if self.inicio is None:
            self.inicio = novo
            novo.proximo = self.inicio
            return

        aux = self.inicio

        while aux.proximo != self.inicio:
            aux = aux.proximo

        aux.proximo = novo
        novo.proximo = self.inicio

    def listar_todos(self):
        if self.inicio is None:
            print("Nenhum deploy cadastrado.")
            return

        print("\nDEPLOYS CADASTRADOS:")

        aux = self.inicio

        while True:
            if aux.ativo:
                status = "Ativo"
            else:
                status = "Inativo"

            print(
                "Nome:", aux.nome,
                "| Duração:", aux.duracao, "segundos",
                "| Ambiente:", aux.ambiente,
                "| Status:", status
            )

            aux = aux.proximo

            if aux == self.inicio:
                break

    def listar_por_ambiente(self):
        ambientes = ["teste", "homologação", "produção"]

        print("\nDEPLOYS POR AMBIENTE:")

        for ambiente in ambientes:

            print("\n---", ambiente.upper(), "---")

            if self.inicio is None:
                continue

            aux = self.inicio
            encontrou = False

            while True:
                if aux.ambiente == ambiente:
                    if aux.ativo:
                        status = "Ativo"
                    else:
                        status = "Inativo"

                    print(
                        "Nome:", aux.nome,
                        "| Duração:", aux.duracao,
                        "segundos",
                        "| Status:", status
                    )

                    encontrou = True

                aux = aux.proximo

                if aux == self.inicio:
                    break

            if not encontrou:
                print("Nenhum deploy nesse ambiente.")

    def listar_ativos(self):
        if self.inicio is None:
            print("Nenhum deploy cadastrado.")
            return

        print("\nDEPLOYS ATIVOS:")

        aux = self.inicio
        encontrou = False

        while True:
            if aux.ativo:
                print(
                    "Nome:", aux.nome,
                    "| Duração:", aux.duracao,
                    "segundos",
                    "| Ambiente:", aux.ambiente
                )

                encontrou = True

            aux = aux.proximo

            if aux == self.inicio:
                break

        if not encontrou:
            print("Nenhum deploy ativo.")

    def tempo_total(self):
        if self.inicio is None:
            return 0

        total = 0
        aux = self.inicio

        while True:
            total += aux.duracao
            aux = aux.proximo

            if aux == self.inicio:
                break

        return total

    def ativar(self, nome):
        if self.inicio is None:
            print("Nenhum deploy cadastrado.")
            return

        aux = self.inicio

        while True:
            if aux.nome == nome:
                aux.ativo = True
                print("Deploy ativado.")
                return

            aux = aux.proximo

            if aux == self.inicio:
                break

        print("Deploy não encontrado.")

    def desativar(self, nome):
        if self.inicio is None:
            print("Nenhum deploy cadastrado.")
            return

        aux = self.inicio

        while True:
            if aux.nome == nome:
                aux.ativo = False
                print("Deploy desativado.")
                return

            aux = aux.proximo

            if aux == self.inicio:
                break

        print("Deploy não encontrado.")

    def excluir(self, nome):
        if self.inicio is None:
            print("Nenhum deploy cadastrado.")
            return

        if self.inicio.proximo == self.inicio:

            if self.inicio.nome == nome:
                self.inicio = None
                print("Deploy excluído.")
                return

            print("Deploy não encontrado.")
            return

        if self.inicio.nome == nome:

            aux = self.inicio

            while aux.proximo != self.inicio:
                aux = aux.proximo

            self.inicio = self.inicio.proximo
            aux.proximo = self.inicio

            print("Deploy excluído.")
            return

        aux = self.inicio

        while aux.proximo != self.inicio:

            if aux.proximo.nome == nome:
                aux.proximo = aux.proximo.proximo
                print("Deploy excluído.")
                return

            aux = aux.proximo

        print("Deploy não encontrado.")

lista = ListaCircular()

while True:

    print("\n==============================")
    print("       MENU DE DEPLOYS")
    print("==============================")
    print("1 - Adicionar deploy")
    print("2 - Listar todos os deploys")
    print("3 - Listar por ambiente")
    print("4 - Listar apenas os ativos")
    print("5 - Exibir tempo total")
    print("6 - Ativar deploy")
    print("7 - Desativar deploy")
    print("8 - Excluir deploy")
    print("9 - Sair")
    print("==============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do deploy: ")

        duracao = int(input("Duração em segundos: "))

        ambiente = input(
            "Ambiente (teste, homologação ou produção): "
        ).lower()

        if ambiente == "teste" or ambiente == "homologação" or ambiente == "produção":
            lista.adicionar(nome, duracao, ambiente)
            print("Deploy adicionado.")
        else:
            print("Ambiente inválido.")

    elif opcao == "2":
        lista.listar_todos()

    elif opcao == "3":
        lista.listar_por_ambiente()

    elif opcao == "4":
        lista.listar_ativos()

    elif opcao == "5":
        total = lista.tempo_total()
        print("Tempo total dos deploys:", total, "segundos")

    elif opcao == "6":
        nome = input("Nome do deploy para ativar: ")
        lista.ativar(nome)

    elif opcao == "7":
        nome = input("Nome do deploy para desativar: ")
        lista.desativar(nome)

    elif opcao == "8":
        nome = input("Nome do deploy para excluir: ")
        lista.excluir(nome)

    elif opcao == "9":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
