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
        print("Não há clientes na fila.")
        return fila

    print("\nCliente atendido:", fila.nome)

    fila = fila.prox

    if fila is not None:
        print("Próximo cliente:", fila.nome)
    else:
        print("Não há mais clientes na fila.")

    return fila


def quantidade(fila):
    cont = 0
    aux = fila

    while aux is not None:
        cont += 1
        aux = aux.prox

    return cont


fila = None

while True:
    print("\n===== BANCO =====")
    print("1 - Inserir cliente")
    print("2 - Atender cliente")
    print("3 - Mostrar quantidade e próximo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do cliente: ")

        fila = inserir(fila, nome)

        print("Cliente inserido na fila.")

    elif opcao == 2:
        fila = atender(fila)

        print("Ainda aguardam:", quantidade(fila))

    elif opcao == 3:
        print("Clientes aguardando:", quantidade(fila))

        if fila is not None:
            print("Próximo da fila:", fila.nome)
        else:
            print("Não há clientes aguardando.")

    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
