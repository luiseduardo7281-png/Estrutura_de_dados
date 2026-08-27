class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.ant = None
        self.prox = None

def inserir(lista, id, nome, artista, duracao):
    novo = No(id, nome, artista, duracao)
    if lista is None:
        return novo

    aux = lista
    while aux.prox is not None:
        aux = aux.prox

    aux.prox = novo
    novo.ant = aux
    return lista

def listar(lista):
    if lista is None:
        print("\nPlaylist vazia!")
        return

    aux = lista
    print("\n========== PLAYLIST ==========")

    while aux is not None:
        print(f"ID: {aux.id}")
        print(f"Música: {aux.nome}")
        print(f"Artista: {aux.artista}")
        print(f"Duração: {aux.duracao:.2f} minutos")
        print("------------------------------")
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

def buscar_artista(lista, artista):
    aux = lista
    while aux is not None:
        if aux.artista.lower() == artista.lower():
            return aux
        aux = aux.prox
    return None

def remover(lista, id):
    aux = buscar_id(lista, id)

    if aux is None:
        print("\nMúsica não encontrada!")
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

def buscar_musica(lista):
    while True:
        print("\n--- BUSCAR MÚSICA ---")
        print("1. Buscar por nome")
        print("2. Buscar por artista")
        print("3. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome da música: ")
            musica = buscar_nome(lista, nome)

            if musica is None:
                print("Música não encontrada!")
            else:
                print("\nMúsica encontrada!")
                print(f"ID: {musica.id}")
                print(f"Nome: {musica.nome}")
                print(f"Artista: {musica.artista}")
                print(f"Duração: {musica.duracao:.2f} minutos")

        elif opcao == "2":
            artista = input("Nome do artista: ")
            musica = buscar_artista(lista, artista)

            if musica is None:
                print("Nenhuma música desse artista foi encontrada!")
            else:
                print("\nMúsica encontrada!")
                print(f"ID: {musica.id}")
                print(f"Nome: {musica.nome}")
                print(f"Artista: {musica.artista}")
                print(f"Duração: {musica.duracao:.2f} minutos")

        elif opcao == "3":
            break

        else:
            print("Opção inválida!")

def duracao_total(lista):
    aux = lista
    total = 0
    while aux is not None:
        total += aux.duracao
        aux = aux.prox

    print(f"\nDuração total da playlist: {total:.2f} minutos")

def navegar(lista):
    if lista is None:
        print("\nPlaylist vazia!")
        return
    aux = lista

    while True:
        print("\n--- MÚSICA ATUAL ---")
        print(f"ID: {aux.id}")
        print(f"Música: {aux.nome}")
        print(f"Artista: {aux.artista}")
        print(f"Duração: {aux.duracao:.2f} minutos")
        print("\n1. Próxima música")
        print("2. Música anterior")
        print("3. Voltar ao menu")
        opcao = input("Escolha: ")

        if opcao == "1":
            if aux.prox is not None:
                aux = aux.prox
            else:
                print("Você está na última música.")

        elif opcao == "2":
            if aux.ant is not None:
                aux = aux.ant
            else:
                print("Você está na primeira música.")

        elif opcao == "3":
            break

        else:
            print("Opção inválida!")

def main():
    lista = None
    while True:
        print("\n========== PLAYLIST ==========")
        print("1. Adicionar música")
        print("2. Listar todas as músicas")
        print("3. Remover música")
        print("4. Buscar música")
        print("5. Mostrar duração total")
        print("6. Avançar / Voltar")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = int(input("ID da música: "))
            nome = input("Nome da música: ")
            artista = input("Artista: ")
            duracao = float(input("Duração em minutos: "))
            lista = inserir(lista, id, nome, artista, duracao)
            print("Música adicionada com sucesso!")

        elif opcao == "2":
            listar(lista)

        elif opcao == "3":
            id = int(input("ID da música a remover: "))
            lista = remover(lista, id)

        elif opcao == "4":
            buscar_musica(lista)

        elif opcao == "5":
            duracao_total(lista)

        elif opcao == "6":
            navegar(lista)

        elif opcao == "7":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


main()
