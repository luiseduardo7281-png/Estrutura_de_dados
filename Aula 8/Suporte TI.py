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


def retirar(fila):
    if fila is None:
        print("Não existem chamados na fila.")
        return fila

    print("\nChamado atendido:", fila.nome)

    fila = fila.prox

    return fila


def quantidade(fila):
    cont = 0
    aux = fila

    while aux is not None:
        cont += 1
        aux = aux.prox

    return cont


def mostrar_fila(fila):
    if fila is None:
        print("Não existem chamados aguardando.")
        return

    aux = fila

    print("\n===== CHAMADOS =====")

    while aux is not None:
        print(aux.nome)
        aux = aux.prox


fila = None

while True:
    print("\n===== SUPORTE DE TI =====")
    print("1 - Registrar chamado")
    print("2 - Atender chamado")
    print("3 - Mostrar fila")
    print("4 - Mostrar quantidade e próximo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome da pessoa: ")

        fila = inserir(fila, nome)

        print("Chamado registrado.")

    elif opcao == 2:
        fila = retirar(fila)

    elif opcao == 3:
        mostrar_fila(fila)

    elif opcao == 4:
        print("Chamados aguardando:", quantidade(fila))

        if fila is not None:
            print("Próximo chamado:", fila.nome)
        else:
            print("Não há chamados aguardando.")

    elif opcao == 5:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
