class No:

    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


def adicionar(lista, nome):

    novo = No(nome)

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


def remover(lista, nome):

    if lista == None:
        print("Lista vazia")
        return lista

    aux = lista

    while 1:

        if aux.nome == nome:

            if aux.proximo == aux:
                print("Cliente removido")
                return None

            if aux == lista:
                lista = lista.proximo

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            print("Cliente saiu do rodízio")

            return lista

        aux = aux.proximo

        if aux == lista:
            break

    print("Cliente não encontrado")

    return lista


def passar_pizza(lista, quantidade):

    if lista == None:
        print("Nenhum cliente")
        return

    aux = lista
    contador = 0

    while contador < quantidade:

        print(aux.nome, "recebeu a fatia de pizza")

        aux = aux.proximo

        contador = contador + 1


def listar(lista):

    if lista == None:
        print("Lista vazia")
        return

    aux = lista

    while 1:

        print("Cliente:", aux.nome)

        aux = aux.proximo

        if aux == lista:
            break


def main():

    lista = None
    opcao = 0

    while opcao != 5:

        print("\n1 - Adicionar cliente")
        print("2 - Remover cliente")
        print("3 - Listar clientes")
        print("4 - Passar pizza")
        print("5 - Sair")

        opcao = int(input("Opção: "))

        if opcao == 1:

            nome = input("Nome: ")
            lista = adicionar(lista, nome)

        elif opcao == 2:

            nome = input("Cliente que saiu: ")
            lista = remover(lista, nome)

        elif opcao == 3:

            listar(lista)

        elif opcao == 4:

            quantidade = int(input("Quantas vezes a pizza será passada: "))
            passar_pizza(lista, quantidade)


main()
