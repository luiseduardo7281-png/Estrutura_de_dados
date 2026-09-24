class Pilha:
    def __init__(self):
        self.dados = []

    def empilhar(self, dado):
        self.dados.append(dado)

    def desempilhar(self):
        if self.esta_vazia():
            print("A pilha está vazia.")
            return None

        return self.dados.pop()

    def percorrer(self):
        for i in range(len(self.dados) - 1, -1, -1):
            print(self.dados[i])

    def topo(self):
        if self.esta_vazia():
            return None

        return self.dados[-1]

    def esta_vazia(self):
        return len(self.dados) == 0

    def tamanho(self):
        return len(self.dados)

    def media(self):
        if self.esta_vazia():
            return 0

        soma = 0

        for valor in self.dados:
            soma += valor

        return soma / len(self.dados)

pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.empilhar(40)

print("PILHA:")
pilha.percorrer()

print("\nTopo:", pilha.topo())
print("Tamanho:", pilha.tamanho())
print("Média:", pilha.media())
print("Está vazia?", pilha.esta_vazia())

print("\nDesempilhando:", pilha.desempilhar())

print("\nPILHA APÓS DESEMPILHAR:")
pilha.percorrer()

print("\nNovo topo:", pilha.topo())
print("Novo tamanho:", pilha.tamanho())
print("Nova média:", pilha.media())
