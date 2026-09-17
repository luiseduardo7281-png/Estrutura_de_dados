class No:
    def __init__(self, operacao):
        self.operacao = operacao
        self.prox = None


def push(pilha, operacao):
    novo = No(operacao)

    novo.prox = pilha

    return novo


def pop(pilha):
    if pilha is None:
        print("Não há operações na pilha.")
        return pilha

    print("Operação retirada:", pilha.operacao)

    return pilha.prox


def topo(pilha):
    if pilha is None:
        print("Não há operações na pilha.")
    else:
        print("Última operação:", pilha.operacao)


def listar(pilha):
    if pilha is None:
        print("Não há operações pendentes.")
        return

    aux = pilha

    print("\n===== OPERAÇÕES PENDENTES =====")

    while aux is not None:
        print(aux.operacao)
        aux = aux.prox


pilha = None

while True:
    print("\n===== OPERAÇÕES MATEMÁTICAS =====")
    print("1 - Inserir operação")
    print("2 - Retirar última operação")
    print("3 - Mostrar última operação")
    print("4 - Mostrar todas as operações")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        operacao = input("Digite a operação: ")

        pilha = push(pilha, operacao)

        print("Operação inserida.")

    elif opcao == 2:
        pilha = pop(pilha)

    elif opcao == 3:
        topo(pilha)

    elif opcao == 4:
        listar(pilha)

    elif opcao == 5:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
