class Fila:
    def __init__(self):
        self.dados = []

    def enfileirar(self, usuario, tempo=0):
        self.dados.append([usuario, tempo])

    def desenfileirar(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return None

        return self.dados.pop(0)

    def percorrer(self):
        for item in self.dados:
            print("Usuário:", item[0], "| Tempo:", item[1], "minutos")

    def frente(self):
        if self.esta_vazia():
            return None

        return self.dados[0]

    def esta_vazia(self):
        return len(self.dados) == 0

    def tamanho(self):
        return len(self.dados)

    def media_tempo(self):
        if self.esta_vazia():
            return 0

        soma = 0

        for item in self.dados:
            soma += item[1]

        return soma / len(self.dados)

fila = Fila()

fila.enfileirar("João", 10)
fila.enfileirar("Maria", 15)
fila.enfileirar("Pedro", 20)
fila.enfileirar("Ana", 5)

print("FILA:")
fila.percorrer()

print("\nPróximo usuário:")
print(fila.frente())

print("\nEstá vazia?", fila.esta_vazia())

print("Tamanho da fila:", fila.tamanho())
print("Média do tempo de espera:", fila.media_tempo(), "minutos")

print("\nAtendendo:")
print(fila.desenfileirar())

print("\nFila após atendimento:")
fila.percorrer()

print("\nPróximo usuário:")
print(fila.frente())

print("\nNovo tamanho:", fila.tamanho())
print("Nova média de espera:", fila.media_tempo(), "minutos")
