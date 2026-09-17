class No:
    def __init__(self, pagina):
        self.pagina = pagina
        self.prox = None


def push(pilha, pagina):
    novo = No(pagina)

    novo.prox = pilha

    return novo


def pop(pilha):
    if pilha is None:
        print("O histórico está vazio.")
        return pilha

    print("Voltando da página:", pilha.pagina)

    return pilha.prox


def topo(pilha):
    if pilha is None:
        print("O histórico está vazio.")
    else:
        print("Página atual:", pilha.pagina)


def listar(pilha):
    if pilha is None:
        print("O histórico está vazio.")
        return

    aux = pilha

    print("\n===== HISTÓRICO =====")

    while aux is not None:
        print(aux.pagina)
        aux = aux.prox


pilha = None

while True:
    print("\n===== HISTÓRICO DO NAVEGADOR =====")
    print("1 - Visitar nova página")
    print("2 - Voltar para página anterior")
    print("3 - Mostrar página atual")
    print("4 - Listar todo o histórico")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        pagina = input("Digite o endereço da página: ")
        pilha = push(pilha, pagina)

        print("Página acessada:", pagina)

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
