class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


def inserir(lista, dado):

    novo = No(dado)

    if lista == None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista

    ultimo = lista.anterior

    novo.proximo = lista
    novo.anterior = ultimo

    ultimo.proximo = novo
    lista.anterior = novo

    lista = novo

    return lista


def listar(lista):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista

    while 1:
        print(aux.dado)

        aux = aux.proximo

        if aux == lista:
            break


def buscar(lista, dado):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista

    while 1:

        if aux.dado == dado:
            print("Dado encontrado:", aux.dado)
            return

        aux = aux.proximo

        if aux == lista:
            break

    print("Dado não encontrado")


def remover(lista, dado):

    if lista == None:
        print("Lista vazia")
        return lista

    aux = lista

    while 1:

        if aux.dado == dado:

            # Só existe um elemento
            if aux.proximo == aux:
                lista = None
                return lista

            # Remover o primeiro
            if aux == lista:
                lista = lista.proximo

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            print("Dado removido")

            return lista

        aux = aux.proximo

        if aux == lista:
            break

    print("Dado não encontrado")

    return lista


def inserir_fim(lista, dado):

    novo = No(dado)

    if lista == None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista

    ultimo = lista.anterior

    novo.proximo = lista
    novo.anterior = ultimo

    ultimo.proximo = novo
    lista.anterior = novo

    return lista


def inserir_ordenado(lista, dado):

    novo = No(dado)

    if lista == None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    # Antes do primeiro
    if dado < lista.dado:

        ultimo = lista.anterior

        novo.proximo = lista
        novo.anterior = ultimo

        ultimo.proximo = novo
        lista.anterior = novo

        lista = novo

        return lista

    aux = lista

    while aux.proximo != lista and aux.proximo.dado < dado:
        aux = aux.proximo

    novo.proximo = aux.proximo
    novo.anterior = aux

    aux.proximo.anterior = novo
    aux.proximo = novo

    return lista


def listar_inverso(lista):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista.anterior

    while 1:

        print(aux.dado)

        if aux == lista:
            break

        aux = aux.anterior


def main():

    lista = None
    opcao = 0

    while opcao != 8:

        print("\n1 - Inserir")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Remover")
        print("5 - Inserir no fim")
        print("6 - Inserir ordenado")
        print("7 - Listar inverso")
        print("8 - Sair")

        opcao = int(input("Opção: "))

        if opcao == 1:
            dado = int(input("Dado: "))
            lista = inserir(lista, dado)

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:
            dado = int(input("Dado para buscar: "))
            buscar(lista, dado)

        elif opcao == 4:
            dado = int(input("Dado para remover: "))
            lista = remover(lista, dado)

        elif opcao == 5:
            dado = int(input("Dado: "))
            lista = inserir_fim(lista, dado)

        elif opcao == 6:
            dado = int(input("Dado: "))
            lista = inserir_ordenado(lista, dado)

        elif opcao == 7:
            listar_inverso(lista)


main()
