class No:

    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None


def inserir(lista, nome, idade, prioridade):

    novo = No(nome, idade, prioridade)

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


def mostrar(lista):

    if lista == None:
        print("Nenhum paciente na fila")
        return

    aux = lista

    while 1:

        print("\nNome:", aux.nome)
        print("Idade:", aux.idade)

        if aux.prioridade == 1:
            print("Prioridade: Emergência")

        elif aux.prioridade == 2:
            print("Prioridade: Urgente")

        else:
            print("Prioridade: Normal")

        aux = aux.proximo

        if aux == lista:
            break


def atender_prioridade(lista, prioridade):

    if lista == None:
        return lista

    aux = lista

    while 1:

        proximo = aux.proximo

        if aux.prioridade == prioridade:

            print("\nPaciente atendido:", aux.nome)

            lista = remover(lista, aux)

            if lista == None:
                return lista

        aux = proximo

        if aux == lista:
            break

    return lista


def atendimento(lista):

    if lista == None:
        print("Nenhum paciente na fila")
        return lista

    print("\n--- INICIANDO ATENDIMENTO ---")

    # Primeiro emergências
    lista = atender_prioridade(lista, 1)

    # Depois urgentes
    lista = atender_prioridade(lista, 2)

    # Depois normais
    lista = atender_prioridade(lista, 3)

    print("\nTodos os pacientes foram atendidos")

    return lista


def main():

    lista = None
    opcao = 0

    while opcao != 4:

        print("\n1 - Inserir paciente")
        print("2 - Mostrar pacientes")
        print("3 - Simular atendimento")
        print("4 - Sair")

        opcao = int(input("Opção: "))

        if opcao == 1:

            nome = input("Nome: ")
            idade = int(input("Idade: "))

            print("\n1 - Emergência")
            print("2 - Urgente")
            print("3 - Normal")

            prioridade = int(input("Prioridade: "))

            if prioridade >= 1 and prioridade <= 3:
                lista = inserir(lista, nome, idade, prioridade)
            else:
                print("Prioridade inválida")

        elif opcao == 2:

            mostrar(lista)

        elif opcao == 3:

            lista = atendimento(lista)


main()
