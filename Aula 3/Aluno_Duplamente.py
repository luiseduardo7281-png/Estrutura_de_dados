class No:
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Buscar aluno")
    print("5 - Listar alunos classificados")
    print("6 - Sair")
    opcao = int(input("Digite a opção: "))
    return opcao

def inserir(lista, id, nome, nota):
    novo = No(id, nome, nota)

    if lista == None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo

    return lista

def listar(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while aux != None:
        if aux == lista:
            print("ANTERIOR: None")
        else:
            print("ANTERIOR:", aux.anterior.id)

        print("ID:", aux.id)
        print("NOME:", aux.nome)
        print("NOTA:", aux.nota)

        if aux.proximo == None:
            print("PRÓXIMO: None")
        else:
            print("PRÓXIMO:", aux.proximo.id)

        print("-------------------------")
        aux = aux.proximo

def buscar(lista, id):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    while aux != None:

        if aux.id == id:
            print("\nAluno encontrado!")
            print("ID:", aux.id)
            print("Nome:", aux.nome)
            print("Nota:", aux.nota)
            return
        aux = aux.proximo

    print("Aluno não encontrado.")

def remover(lista, id):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return lista

    while aux != None:
        if aux.id == id:

            if aux.proximo == None and aux.anterior == None:
                lista = None
                print("Aluno removido!")
                return lista

            elif aux == lista:
                lista = lista.proximo
                lista.anterior = None
                print("Aluno removido!")
                return lista

            elif aux.proximo == None:
                aux.anterior.proximo = None
                print("Aluno removido!")
                return lista

            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                print("Aluno removido!")
                return lista

        aux = aux.proximo

    print("Aluno não encontrado.")
    return lista

def classificados(lista):
    aux = lista

    if lista == None:
        print("Lista vazia")
        return

    print("\nCLASSIFICAÇÃO")
    print("1 - Aprovado")
    print("2 - Exame")
    print("3 - Reprovado")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        print("\nAPROVADOS")
    elif opcao == 2:
        print("\nEXAME")
    elif opcao == 3:
        print("\n REPROVADOS")
    else:
        print("Opção inválida.")
        return
    encontrou = 0

    while aux != None:
        if opcao == 1 and aux.nota >= 7:
            print(
                "ID:", aux.id,
                "| Nome:", aux.nome,
                "| Nota:", aux.nota
            )
            encontrou = 1

        elif opcao == 2 and aux.nota >= 4 and aux.nota < 7:
            print(
                "ID:", aux.id,
                "| Nome:", aux.nome,
                "| Nota:", aux.nota
            )
            encontrou = 1

        elif opcao == 3 and aux.nota < 4:
            print(
                "ID:", aux.id,
                "| Nome:", aux.nome,
                "| Nota:", aux.nota
            )
            encontrou = 1
        aux = aux.proximo

    if encontrou == 0:
        print("Nenhum aluno encontrado nessa categoria.")

def main():
    lista = None
    opcao = 0

    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            id = int(input("ID do aluno: "))
            nome = input("Nome do aluno: ")
            nota = float(input("Nota final: "))
            if nota < 0 or nota > 10:
                print("Nota inválida!")
            else:
                lista = inserir(lista, id, nome, nota)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            id = int(input("ID do aluno para remover: "))
            lista = remover(lista, id)
        elif opcao == 4:
            id = int(input("ID do aluno para buscar: "))
            buscar(lista, id)
        elif opcao == 5:
            classificados(lista)
        else:
            print("Opção inválida.")

main()
