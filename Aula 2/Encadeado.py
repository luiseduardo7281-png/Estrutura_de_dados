class No:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

def inserir(lista, valor):
    novo = No(float(valor))

    if lista is None:
        return novo

    atual = lista

    while atual.prox is not None:
        atual = atual.prox

    atual.prox = novo

    return lista

def listar(lista):
    if lista is None:
        print("Lista vazia!")
        return

    atual = lista

    while atual is not None:
        print(atual.info)
        atual = atual.prox

def remover(lista, valor):
    if lista is None:
        return lista

    if lista.info == valor:
        return lista.prox

    atual = lista

    while atual.prox is not None:
        if atual.prox.info == valor:
            atual.prox = atual.prox.prox
            return lista

        atual = atual.prox

    return lista

def maiores(lst, n):
    quantidade = 0
    atual = lst

    while atual is not None:
        if atual.info > n:
            quantidade += 1

        atual = atual.prox

    return quantidade

def ultimo(lista):
    if lista is None:
        return None

    atual = lista

    while atual.prox is not None:
        atual = atual.prox

    return atual

def lista_insere_final(lst, valor):
    novo = No(valor)

    if lst is None:
        return novo

    atual = lst

    while atual.prox is not None:
        atual = atual.prox

    atual.prox = novo

    return lst

def lista_calcula_media(lst):
    if lst is None:
        return 0

    soma = 0
    quantidade = 0
    atual = lst

    while atual is not None:
        soma += atual.info
        quantidade += 1
        atual = atual.prox

    return soma / quantidade

def lista_altera(lst):
    atual = lst

    while atual is not None:
        atual.info = atual.info * -1
        atual = atual.prox

    return lst

lista = None

while True:

    print("\n----- MENU -----")
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Remover item")
    print("4 - Contar valores maiores que N")
    print("5 - Mostrar último item")
    print("6 - Inserir item no final")
    print("7 - Calcular média")
    print("8 - Alterar sinais")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor: "))
        lista = inserir(lista, valor)
        print("Item inserido!")

    elif opcao == 2:
        print("\nItens da lista:")
        listar(lista)

    elif opcao == 3:
        valor = float(input("Digite o valor que deseja remover: "))
        lista = remover(lista, valor)
        print("Operação realizada!")

    elif opcao == 4:
        n = float(input("Digite o valor de N: "))
        resultado = maiores(lista, n)
        print("Quantidade de valores maiores que", n, ":", resultado)

    elif opcao == 5:
        no = ultimo(lista)

        if no is None:
            print("A lista está vazia!")
        else:
            print("Último item da lista:", no.info)

    elif opcao == 6:
        valor = float(input("Digite o valor: "))
        lista = lista_insere_final(lista, valor)
        print("Item inserido no final!")

    elif opcao == 7:
        media = lista_calcula_media(lista)

        if lista is None:
            print("A lista está vazia!")
        else:
            print("Média dos valores:", media)

    elif opcao == 8:
        lista = lista_altera(lista)
        print("Sinais dos valores foram alterados!")

    elif opcao == 0:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
