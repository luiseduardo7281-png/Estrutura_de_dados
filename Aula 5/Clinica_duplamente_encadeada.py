class NoPaciente:
    def __init__(self, codigo, nome, idade, prioridade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.ant = None
        self.prox = None


prioridades = {
    1: "Emergência",
    2: "Muito urgente",
    3: "Urgente",
    4: "Pouco urgente",
    5: "Não urgente"
}


# Escolher prioridade
def escolher_prioridade():
    print("\nPrioridade:")
    print("1 - Emergência")
    print("2 - Muito urgente")
    print("3 - Urgente")
    print("4 - Pouco urgente")
    print("5 - Não urgente")

    prioridade = int(input("Escolha a prioridade: "))

    while prioridade < 1 or prioridade > 5:
        print("Prioridade inválida.")
        prioridade = int(input("Escolha a prioridade: "))

    return prioridade


# Cadastrar paciente no final
def cadastrar_paciente(lista, codigo, nome, idade, prioridade):
    novo = NoPaciente(codigo, nome, idade, prioridade)

    if lista is None:
        return novo

    aux = lista

    while aux.prox is not None:
        aux = aux.prox

    aux.prox = novo
    novo.ant = aux

    return lista


# Buscar paciente pelo código
def buscar_paciente(lista, codigo):
    aux = lista

    while aux is not None:
        if aux.codigo == codigo:
            return aux

        aux = aux.prox

    return None


# Remover paciente pelo código
def remover_paciente(lista, codigo):
    aux = lista

    while aux is not None:

        if aux.codigo == codigo:

            # Primeiro elemento
            if aux.ant is None:
                lista = aux.prox

                if lista is not None:
                    lista.ant = None

                return lista

            # Elemento do meio ou último
            aux.ant.prox = aux.prox

            if aux.prox is not None:
                aux.prox.ant = aux.ant

            return lista

        aux = aux.prox

    return lista


# Atender o paciente mais urgente
def atender_mais_urgente(lista):
    if lista is None:
        print("Não há pacientes aguardando atendimento.")
        return lista

    aux = lista
    mais_urgente = lista

    while aux is not None:

        if aux.prioridade < mais_urgente.prioridade:
            mais_urgente = aux

        aux = aux.prox

    print("\nPaciente atendido:")
    print("Código:", mais_urgente.codigo)
    print("Nome:", mais_urgente.nome)
    print("Idade:", mais_urgente.idade)
    print("Prioridade:", prioridades[mais_urgente.prioridade])

    lista = remover_paciente(lista, mais_urgente.codigo)

    return lista


# Listar do primeiro para o último
def listar_primeiro_ultimo(lista):
    if lista is None:
        print("Nenhum paciente aguardando.")
        return

    aux = lista

    while aux is not None:
        print("-----------------------------")
        print("Código:", aux.codigo)
        print("Nome:", aux.nome)
        print("Idade:", aux.idade)
        print("Prioridade:", prioridades[aux.prioridade])

        aux = aux.prox

    print("-----------------------------")


# Listar pacientes de uma determinada prioridade
def listar_por_prioridade(lista, prioridade):
    aux = lista
    encontrou = False

    while aux is not None:

        if aux.prioridade == prioridade:
            print("-----------------------------")
            print("Código:", aux.codigo)
            print("Nome:", aux.nome)
            print("Idade:", aux.idade)
            print("Prioridade:", prioridades[aux.prioridade])

            encontrou = True

        aux = aux.prox

    if not encontrou:
        print("Nenhum paciente com essa prioridade.")


# Listar do último para o primeiro
def listar_ultimo_primeiro(lista):
    if lista is None:
        print("Nenhum paciente aguardando.")
        return

    aux = lista

    # Vai até o último nó
    while aux.prox is not None:
        aux = aux.prox

    # Volta usando o ponteiro ant
    while aux is not None:
        print("-----------------------------")
        print("Código:", aux.codigo)
        print("Nome:", aux.nome)
        print("Idade:", aux.idade)
        print("Prioridade:", prioridades[aux.prioridade])

        aux = aux.ant

    print("-----------------------------")


# Contar pacientes aguardando
def quantidade_pacientes(lista):
    quantidade = 0
    aux = lista

    while aux is not None:
        quantidade += 1
        aux = aux.prox

    return quantidade


# ==========================================================
# HISTÓRICO DE PÁGINAS
# ==========================================================

class NoPagina:
    def __init__(self, pagina):
        self.pagina = pagina
        self.ant = None
        self.prox = None


# Acessar uma nova página
def acessar_pagina(historico, atual, pagina):

    novo = NoPagina(pagina)

    # Primeiro acesso
    if historico is None:
        return novo, novo

    # Se o usuário voltou e acessou uma nova página,
    # todas as páginas que estavam à frente são removidas.
    if atual is not None:

        aux = atual.prox

        while aux is not None:
            proximo = aux.prox
            aux.ant = None
            aux.prox = None
            aux = proximo

        atual.prox = None

        novo.ant = atual
        atual.prox = novo

        return historico, novo

    # Caso não exista página atual
    aux = historico

    while aux.prox is not None:
        aux = aux.prox

    aux.prox = novo
    novo.ant = aux

    return historico, novo


# Voltar uma página
def voltar_pagina(atual):
    if atual is None:
        print("Não existe página no histórico.")
        return atual

    if atual.ant is None:
        print("Você já está na primeira página.")
        return atual

    atual = atual.ant

    print("Página atual:", atual.pagina)

    return atual


# Avançar uma página
def avancar_pagina(atual):
    if atual is None:
        print("Não existe página no histórico.")
        return atual

    if atual.prox is None:
        print("Você já está na última página.")
        return atual

    atual = atual.prox

    print("Página atual:", atual.pagina)

    return atual


# Mostrar histórico
def mostrar_historico(historico, atual):
    if historico is None:
        print("Histórico vazio.")
        return

    aux = historico

    print("\n========== HISTÓRICO ==========")

    while aux is not None:

        if aux == atual:
            print("->", aux.pagina, "(ATUAL)")
        else:
            print("  ", aux.pagina)

        aux = aux.prox


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

lista = None

historico = None
pagina_atual = None

while True:

    print("\n========== CLÍNICA ==========")
    print("1 - Cadastrar paciente")
    print("2 - Remover paciente após atendimento")
    print("3 - Localizar paciente pelo código")
    print("4 - Atender paciente mais urgente")
    print("5 - Listar pacientes (primeiro ao último)")
    print("6 - Listar por prioridade")
    print("7 - Listar pacientes (último ao primeiro)")
    print("8 - Quantidade de pacientes aguardando")
    print("9 - Histórico de páginas")
    print("10 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        codigo = int(input("Digite o código do paciente: "))

        if buscar_paciente(lista, codigo) is not None:
            print("Esse código já está cadastrado.")
        else:
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            prioridade = escolher_prioridade()

            lista = cadastrar_paciente(
                lista,
                codigo,
                nome,
                idade,
                prioridade
            )

            print("Paciente cadastrado com sucesso!")

    elif opcao == 2:

        codigo = int(input("Digite o código do paciente que será removido: "))

        paciente = buscar_paciente(lista, codigo)

        if paciente is None:
            print("Paciente não encontrado.")
        else:
            lista = remover_paciente(lista, codigo)
            print("Paciente removido após atendimento.")

    elif opcao == 3:

        codigo = int(input("Digite o código do paciente: "))

        paciente = buscar_paciente(lista, codigo)

        if paciente is None:
            print("Paciente não encontrado.")
        else:
            print("\nPaciente encontrado!")
            print("Código:", paciente.codigo)
            print("Nome:", paciente.nome)
            print("Idade:", paciente.idade)
            print("Prioridade:", prioridades[paciente.prioridade])

    elif opcao == 4:

        lista = atender_mais_urgente(lista)

    elif opcao == 5:

        listar_primeiro_ultimo(lista)

    elif opcao == 6:

        prioridade = escolher_prioridade()
        listar_por_prioridade(lista, prioridade)

    elif opcao == 7:

        listar_ultimo_primeiro(lista)

    elif opcao == 8:

        quantidade = quantidade_pacientes(lista)

        print("Quantidade de pacientes aguardando:", quantidade)

    elif opcao == 9:

        while True:

            print("\n====== HISTÓRICO DE PÁGINAS ======")
            print("1 - Acessar nova página")
            print("2 - Voltar")
            print("3 - Avançar")
            print("4 - Mostrar histórico")
            print("5 - Voltar para o menu da clínica")

            opcao_historico = int(input("Escolha uma opção: "))

            if opcao_historico == 1:

                pagina = input("Digite o endereço da nova página: ")

                historico, pagina_atual = acessar_pagina(
                    historico,
                    pagina_atual,
                    pagina
                )

                print("Página acessada:", pagina_atual.pagina)

            elif opcao_historico == 2:

                pagina_atual = voltar_pagina(pagina_atual)

            elif opcao_historico == 3:

                pagina_atual = avancar_pagina(pagina_atual)

            elif opcao_historico == 4:

                mostrar_historico(historico, pagina_atual)

            elif opcao_historico == 5:

                break

            else:
                print("Opção inválida.")

    elif opcao == 10:

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")
