class No:
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.ant = None
        self.prox = None


def inserir(lista, id, nome, nota):
    novo = No(id, nome, nota)

    novo.prox = lista

    if lista is not None:
        lista.ant = novo

    return novo


def listar(lista):
    if lista is None:
        print("\nLista vazia!")
        return

    aux = lista

    print("\n--- ALUNOS ---")

    while aux is not None:
        print(f"ID: {aux.id}")
        print(f"Nome: {aux.nome}")
        print(f"Nota: {aux.nota:.1f}")
        print("--------------------")

        aux = aux.prox


def buscar(lista, id):
    aux = lista

    while atual is not None:
        if aux.id == id:
            return aux

        aux = aux.prox

    return None


def remover(lista, id):
    aux = buscar(lista, id)

    if aux is None:
        print("\nAluno não encontrado!")
        return aux

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

def buscar_aluno(lista):
    id = int(input("Digite o ID do aluno: "))

    aluno = buscar(lista, id)

    if aluno is None:
        print("\nAluno não encontrado!")
    else:
        print("\n--- ALUNO ENCONTRADO ---")
        print(f"ID: {aluno.id}")
        print(f"Nome: {aluno.nome}")
        print(f"Nota: {aluno.nota:.1f}")

def listar_classificados(lista, tipo):
    aux = lista
    encontrou = False

    while aux is not None:

        if tipo == "aprovado" and aux.nota >= 7:
            print(f"ID: {aux.id} | Nome: {aux.nome} | Nota: {aux.nota:.1f}")
            encontrou = True

        elif tipo == "exame" and aux.nota >= 4 and aux.nota < 7:
            print(f"ID: {aux.id} | Nome: {aux.nome} | Nota: {aux.nota:.1f}")
            encontrou = True

        elif tipo == "reprovado" and aux.nota < 4:
            print(f"ID: {aux.id} | Nome: {aux.nome} | Nota: {aux.nota:.1f}")
            encontrou = True

        aux = aux.prox

    if not encontrou:
        print("Nenhum aluno encontrado nessa classificação.")

def menu_classificacao(lista):
    while True:
        print("\n--- CLASSIFICAÇÃO ---")
        print("1. Aprovados")
        print("2. Exame")
        print("3. Reprovados")
        print("4. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("\n--- APROVADOS ---")
            listar_classificados(lista, "aprovado")

        elif opcao == "2":
            print("\n--- EXAME ---")
            listar_classificados(lista, "exame")

        elif opcao == "3":
            print("\n--- REPROVADOS ---")
            listar_classificados(lista, "reprovado")

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

def main():
    lista = None

    while True:
        print("\n========== MENU ==========")
        print("1. Inserir aluno")
        print("2. Listar alunos")
        print("3. Remover aluno")
        print("4. Buscar aluno")
        print("5. Classificar alunos")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome: ")
            nota = float(input("Nota final: "))

            lista = inserir(lista, id, nome, nota)
            print("Aluno inserido com sucesso!")

        elif opcao == "2":
            listar(lista)

        elif opcao == "3":
            id = int(input("Digite o ID do aluno a remover: "))
            lista = remover(lista, id)

        elif opcao == "4":
            buscar_aluno(lista)

        elif opcao == "5":
            menu_classificacao(lista)

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")

main()
