import random


class No:

    def __init__(self, guerreiro):
        self.guerreiro = guerreiro
        self.proximo = None
        self.anterior = None


def adicionar(lista, guerreiro):

    novo = No(guerreiro)

    if lista == None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    ultimo = lista.anterior

    novo.proximo = lista
    novo.anterior = ultimo

    ultimo.proximo = novo
    lista.anterior = novo

    return lista


def remover(lista, aux):

    if aux.proximo == aux:
        return None

    if aux == lista:
        lista = lista.proximo

    aux.anterior.proximo = aux.proximo
    aux.proximo.anterior = aux.anterior

    return lista


def contar(lista):

    if lista == None:
        return 0

    quantidade = 1
    aux = lista.proximo

    while aux != lista:
        quantidade = quantidade + 1
        aux = aux.proximo

    return quantidade


def jogar(lista):

    while contar(lista) > 1:

        quantidade = contar(lista)

        sorteado = random.randint(1, quantidade)

        aux = lista
        contador = 1

        while contador < sorteado:
            aux = aux.proximo
            contador = contador + 1

        print("Guerreiro eliminado:", aux.guerreiro)

        lista = remover(lista, aux)

    print("\nSobrevivente:", lista.guerreiro)

    return lista


def main():

    lista = None

    quantidade = int(input("Quantidade de guerreiros: "))

    contador = 1

    while contador <= quantidade:

        nome = input("Nome do guerreiro: ")

        lista = adicionar(lista, nome)

        contador = contador + 1

    jogar(lista)


main()
