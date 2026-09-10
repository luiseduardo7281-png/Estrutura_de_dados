class No:

    def __init__(self, id):
        self.id = id
        self.bastao = 0
        self.proximo = None
        self.anterior = None


def adicionar(lista, id):

    novo = No(id)

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


def remover(lista, id):

    if lista == None:
        print("Lista vazia")
        return lista

    aux = lista

    while 1:

        if aux.id == id:

            if aux.proximo == aux:
                return None

            if aux == lista:
                lista = lista.proximo

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            print("Atleta removido")
            return lista

        aux = aux.proximo

        if aux == lista:
            break

    print("Atleta não encontrado")

    return lista


def passar_bastao(lista, voltas):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista

    contador = 0

    while contador < voltas:

        aux.bastao = 1

        print("Atleta", aux.id, "está com o bastão")

        aux.bastao = 0

        aux = aux.proximo

        contador = contador + 1


def listar(lista):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista

    while 1:

        print("Atleta:", aux.id)

        aux = aux.proximo

        if aux == lista:
            break


def main():

    lista = None
    opcao = 0

    while opcao != 5:

        print("\n1 - Adicionar atleta")
        print("2 - Remover atleta")
        print("3 - Listar atletas")
        print("4 - Passar bastão")
        print("5 - Sair")

        opcao = int(input("Opção: "))

        if opcao == 1:
            id = int(input("ID do atleta: "))
            lista = adicionar(lista, id)

        elif opcao == 2:
            id = int(input("ID para remover: "))
            lista = remover(lista, id)

        elif opcao == 3:
            listar(lista)

        elif opcao == 4:
            voltas = int(input("Quantidade de turnos: "))
            passar_bastao(lista, voltas)


main()
