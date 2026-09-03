class No:
    def __init__(self, matricula, nome, nota):
        self.matricula = matricula
        self.nome = nome
        self.situacao = True
        self.nota = nota
        self.prox = None


# Cadastrar aluno no final da lista
def cadastrar_final(lista, matricula, nome, nota):
    novo = No(matricula, nome, nota)

    if lista is None:
        return novo

    aux = lista

    while aux.prox is not None:
        aux = aux.prox

    aux.prox = novo

    return lista


# Listar todos os alunos
def listar_todos(lista):
    if lista is None:
        print("Nenhum aluno cadastrado.")
        return

    aux = lista

    while aux is not None:
        if aux.situacao:
            situacao = "Ativo"
        else:
            situacao = "Desativado"

        print("-----------------------------")
        print("Matrícula:", aux.matricula)
        print("Nome:", aux.nome)
        print("Nota final:", aux.nota)
        print("Situação:", situacao)

        aux = aux.prox

    print("-----------------------------")


# Listar somente alunos ativos
def listar_ativos(lista):
    aux = lista
    encontrou = False

    while aux is not None:
        if aux.situacao:
            print("-----------------------------")
            print("Matrícula:", aux.matricula)
            print("Nome:", aux.nome)
            print("Nota final:", aux.nota)
            print("Situação: Ativo")
            encontrou = True

        aux = aux.prox

    if not encontrou:
        print("Nenhum aluno ativo cadastrado.")


# Listar somente alunos desativados
def listar_desativados(lista):
    aux = lista
    encontrou = False

    while aux is not None:
        if not aux.situacao:
            print("-----------------------------")
            print("Matrícula:", aux.matricula)
            print("Nome:", aux.nome)
            print("Nota final:", aux.nota)
            print("Situação: Desativado")
            encontrou = True

        aux = aux.prox

    if not encontrou:
        print("Nenhum aluno desativado cadastrado.")


# Buscar aluno pela matrícula
def buscar_matricula(lista, matricula):
    aux = lista

    while aux is not None:
        if aux.matricula == matricula:
            return aux

        aux = aux.prox

    return None


# Alterar nota final
def alterar_nota(lista, matricula, nova_nota):
    aluno = buscar_matricula(lista, matricula)

    if aluno is None:
        return False

    aluno.nota = nova_nota
    return True


# Alterar situação do aluno
def alterar_situacao(lista, matricula):
    aluno = buscar_matricula(lista, matricula)

    if aluno is None:
        return False

    if aluno.situacao:
        aluno.situacao = False
    else:
        aluno.situacao = True

    return True


# Remover aluno pela matrícula
def remover_aluno(lista, matricula):
    if lista is None:
        return None

    # Caso o aluno esteja no primeiro nó
    if lista.matricula == matricula:
        return lista.prox

    aux = lista

    while aux.prox is not None:
        if aux.prox.matricula == matricula:
            aux.prox = aux.prox.prox
            return lista

        aux = aux.prox

    return lista


# Quantidade de alunos cadastrados
def quantidade_cadastrados(lista):
    quantidade = 0
    aux = lista

    while aux is not None:
        quantidade += 1
        aux = aux.prox

    return quantidade


# Média das notas de toda a turma
def media_turma(lista):
    soma = 0
    quantidade = 0
    aux = lista

    while aux is not None:
        soma += aux.nota
        quantidade += 1
        aux = aux.prox

    if quantidade == 0:
        return 0

    return soma / quantidade


# Média das notas dos alunos ativos
def media_ativos(lista):
    soma = 0
    quantidade = 0
    aux = lista

    while aux is not None:
        if aux.situacao:
            soma += aux.nota
            quantidade += 1

        aux = aux.prox

    if quantidade == 0:
        return 0

    return soma / quantidade


# Programa principal
lista = None

while True:
    print("\n========== MENU ==========")
    print("1 - Cadastrar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Listar alunos ativos")
    print("4 - Listar alunos desativados")
    print("5 - Buscar aluno pela matrícula")
    print("6 - Alterar nota final")
    print("7 - Alterar situação")
    print("8 - Remover aluno")
    print("9 - Quantidade de alunos cadastrados")
    print("10 - Média da turma")
    print("11 - Média dos alunos ativos")
    print("12 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        matricula = int(input("Digite a matrícula: "))
        nome = input("Digite o nome: ")
        nota = float(input("Digite a nota final: "))

        if buscar_matricula(lista, matricula) is not None:
            print("Essa matrícula já está cadastrada.")
        else:
            lista = cadastrar_final(lista, matricula, nome, nota)
            print("Aluno cadastrado com sucesso!")
            print("Situação inicial: Ativo")

    elif opcao == 2:
        listar_todos(lista)

    elif opcao == 3:
        listar_ativos(lista)

    elif opcao == 4:
        listar_desativados(lista)

    elif opcao == 5:
        matricula = int(input("Digite a matrícula: "))

        aluno = buscar_matricula(lista, matricula)

        if aluno is None:
            print("Aluno não encontrado.")
        else:
            print("\nAluno encontrado!")
            print("Matrícula:", aluno.matricula)
            print("Nome:", aluno.nome)
            print("Nota:", aluno.nota)

            if aluno.situacao:
                print("Situação: Ativo")
            else:
                print("Situação: Desativado")

    elif opcao == 6:
        matricula = int(input("Digite a matrícula: "))
        nova_nota = float(input("Digite a nova nota: "))

        if alterar_nota(lista, matricula, nova_nota):
            print("Nota alterada com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == 7:
        matricula = int(input("Digite a matrícula: "))

        if alterar_situacao(lista, matricula):
            print("Situação alterada com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == 8:
        matricula = int(input("Digite a matrícula: "))

        aluno = buscar_matricula(lista, matricula)

        if aluno is None:
            print("Aluno não encontrado.")
        else:
            lista = remover_aluno(lista, matricula)
            print("Aluno removido com sucesso!")

    elif opcao == 9:
        quantidade = quantidade_cadastrados(lista)
        print("Quantidade de alunos cadastrados:", quantidade)

    elif opcao == 10:
        media = media_turma(lista)
        print("Média da turma:", media)

    elif opcao == 11:
        media = media_ativos(lista)
        print("Média dos alunos ativos:", media)

    elif opcao == 12:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
