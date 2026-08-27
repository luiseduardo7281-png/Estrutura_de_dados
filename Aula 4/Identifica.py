class No:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.ant = None
        self.prox = None


def inserir(lista, nome, id):
    novo = No(nome, id)
    novo.prox = lista

    if lista is not None:
        lista.ant = novo
    return novo

def listar(lista):
    if lista is None:
        print("\nLista vazia!")
        return
    aux = lista
    print("\n--- NÓS DA LISTA ---")
    
    while aux is not None:
        print(f"Nome: {aux.nome} | ID: {aux.id}")
        aux = aux.prox

def buscar_id(lista, id):
    aux = lista
    while aux is not None:
        if aux.id == id:
            return aux

        aux = aux.prox
    return None

def buscar_nome(lista, nome):
    aux = lista

    while aux is not None:
        if aux.nome.lower() == nome.lower():
            return aux

        aux = aux.prox

    return None

def remover(lista, id):
    aux = buscar_id(lista, id)

    if aux is None:
        print("\nNó não encontrado!")
        return lista

    if aux.ant is None and aux.prox is None:
        return None

    if aux.ant is None:
        aux.prox.ant = None
        return aux.prox

    if aux.prox is None:
        aux.ant.prox = None
        return lista

    aux.ant.prox = aux.prox
    aux.prox.ant = aux.ant

    return lista

def verificar(lista):
    while True:
        print("\n--- BUSCAR NÓ ---")
        print("1. Buscar por nome")
        print("2. Buscar por identificador")
        print("3. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Digite o nome: ")

            no = buscar_nome(lista, nome)

            if no is None:
                print("Nó não encontrado!")
            else:
                print("\nNó encontrado!")
                print(f"Nome: {no.nome}")
                print(f"ID: {no.id}")

        elif opcao == "2":
            id = int(input("Digite o identificador: "))

            no = buscar_id(lista, id)

            if no is None:
                print("Nó não encontrado!")
            else:
                print("\nNó encontrado!")
                print(f"Nome: {no.nome}")
                print(f"ID: {no.id}")

        elif opcao == "3":
            break

        else:
            print("Opção inválida!")

def main():
    lista = None

    while True:
        print("\n========== MENU ==========")
        print("1. Inserir nó")
        print("2. Listar nós")
        print("3. Remover nó")
        print("4. Verificar se nó existe")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            id = int(input("Identificador: "))
            lista = inserir(lista, nome, id)
            print("Nó inserido com sucesso!")

        elif opcao == "2":
            listar(lista)

        elif opcao == "3":
            id = int(input("Digite o identificador do nó: "))
            lista = remover(lista, id)

        elif opcao == "4":
            verificar(lista)

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")

main()
