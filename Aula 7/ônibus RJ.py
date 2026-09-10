class No:

    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None


def adicionar(lista, parada):

    novo = No(parada)

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


def remover(lista, parada):

    if lista == None:
        print("Lista vazia")
        return lista

    aux = lista

    while 1:

        if aux.parada == parada:

            if aux.proximo == aux:
                print("Parada removida")
                return None

            if aux == lista:
                lista = lista.proximo

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            print("Parada removida")

            return lista

        aux = aux.proximo

        if aux == lista:
            break

    print("Parada não encontrada")

    return lista


def percurso(lista, voltas):

    if lista == None:
        print("Nenhuma parada cadastrada")
        return

    aux = lista
    contador = 0

    while contador < voltas:

        print("Ônibus está na parada:", aux.parada)

        aux = aux.proximo

        contador = contador + 1


def listar(lista):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista

    while 1:

        print("Parada:", aux.parada)

        aux = aux.proximo

        if aux == lista:
            break


def main():

    lista = None
    opcao = 0

    while opcao != 5:

        print("\n1 - Adicionar parada")
        print("2 - Remover parada")
        print("3 - Listar paradas")
        print("4 - Simular percurso")
        print("5 - Sair")

        opcao = int(input("Opção: "))

        if opcao == 1:
            parada = input("Nome da parada: ")
            lista = adicionar(lista, parada)

        elif opcao == 2:
            parada = input("Parada para remover: ")
            lista = remover(lista, parada)

        elif opcao == 3:
            listar(lista)

        elif opcao == 4:
            voltas = int(input("Quantidade de paradas a percorrer: "))
            percurso(lista, voltas)


main()
