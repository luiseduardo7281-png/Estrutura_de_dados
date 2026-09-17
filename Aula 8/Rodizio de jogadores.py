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

def rodada(fila):
    if fila is None:
        print("Não há jogadores na fila.")
        return fila

    jogador = fila.nome
  
    fila = fila.prox

    novo = No(jogador)

    if fila is None:
        fila = novo
    else:
        aux = fila

        while aux.prox is not None:
            aux = aux.prox

        aux.prox = novo

    print("Jogador que participou:", jogador)

    return fila


def mostrar_fila(fila):
    if fila is None:
        print("A fila está vazia.")
        return

    aux = fila
    posicao = 1

    print("\n===== FILA =====")

    while aux is not None:
        print(posicao, "-", aux.nome)

        posicao += 1
        aux = aux.prox


def mostrar_proximo(fila):
    if fila is None:
        print("A fila está vazia.")
    else:
        print("Próximo a jogar:", fila.nome)


def limpar(fila):
    fila = None

    print("Fila limpa.")

    return fila


fila = None

while True:

    print("\n===== RODÍZIO DE JOGADORES =====")
    print("1 - Adicionar jogador")
    print("2 - Simular 1 rodada")
    print("3 - Simular N rodadas")
    print("4 - Mostrar fila")
    print("5 - Mostrar próximo a jogar")
    print("6 - Limpar fila")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        nome = input("Nome do jogador: ")

        fila = inserir(fila, nome)

        print("Jogador adicionado.")

    elif opcao == 2:

        fila = rodada(fila)

    elif opcao == 3:

        n = int(input("Quantas rodadas deseja simular? "))

        for i in range(n):
            print("\n--- Rodada", i + 1, "---")

            fila = rodada(fila)

            print("Ordem atual da fila:")
            mostrar_fila(fila)

    elif opcao == 4:

        mostrar_fila(fila)

    elif opcao == 5:

        mostrar_proximo(fila)

    elif opcao == 6:

        fila = limpar(fila)

    elif opcao == 7:

        print("Programa encerrado.")

    else:

        print("Opção inválida.")
