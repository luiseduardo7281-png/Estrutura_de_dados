class No:
    def __init__(self, nome):
        self.nome = nome
        self.prox = None


def inserir(fila, nome):
    novo = No(nome)

    if fila is None:
        return novo

    aux = fila

    while aux.prox is not None:
        aux = aux.prox

    aux.prox = novo

    return fila


def atender(fila):
    if fila is None:
        print("Não há clientes aguardando.")
        return fila

    print("Cliente atendido:", fila.nome)

    return fila.prox


def listar(fila):
    if fila is None:
        print("A fila está vazia.")
        return

    aux = fila

    print("\n===== FILA ATUAL =====")

    while aux is not None:
        print(aux.nome)
        aux = aux.prox


def proximo(fila):
    if fila is None:
        print("A fila está vazia.")
    else:
        print("Próximo a ser atendido:", fila.nome)


fila = None

while True:
    print("\n===== CLÍNICA =====")
    print("1 - Inserir cliente na fila")
    print("2 - Atender cliente")
    print("3 - Mostrar fila atual")
    print("4 - Mostrar próximo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do cliente: ")

        fila = inserir(fila, nome)

        print("Cliente inserido.")

    elif opcao == 2:
        fila = atender(fila)

    elif opcao == 3:
        listar(fila)

    elif opcao == 4:
        proximo(fila)

    elif opcao == 5:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
