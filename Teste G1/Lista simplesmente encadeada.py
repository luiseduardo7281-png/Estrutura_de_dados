class No:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, nome, responsavel):
        novo = No(nome, responsavel)

        if self.inicio is None:
            self.inicio = novo
        else:
            aux = self.inicio

            while aux.proximo is not None:
                aux = aux.proximo

            aux.proximo = novo

    def listar(self):
        if self.inicio is None:
            print("Lista vazia.")
            return

        aux = self.inicio

        while aux is not None:
            print("Sprint:", aux.nome)
            print("Responsável:", aux.responsavel)
            print()

            aux = aux.proximo

    def remover(self, nome):
        if self.inicio is None:
            return

        if self.inicio.nome == nome:
            self.inicio = self.inicio.proximo
            return

        aux = self.inicio

        while aux.proximo is not None:
            if aux.proximo.nome == nome:
                aux.proximo = aux.proximo.proximo
                return

            aux = aux.proximo


lista = ListaEncadeada()

lista.inserir("Planejamento do Produto", "Ana")
lista.inserir("Implementação do Backend", "João")
lista.inserir("Testes Automatizados", "Carla")

print("SPRINTS:")
lista.listar()

lista.remover("Planejamento do Produto")

print("SPRINTS DEPOIS DA REMOÇÃO:")
lista.listar()
