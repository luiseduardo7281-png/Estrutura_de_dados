class No:
    def __init__(self, carro):
        self.carro = carro
        self.prox = None


def push(pilha, carro):
    novo = No(carro)

    novo.prox = pilha

    return novo


def listar(pilha):
    aux = pilha

    while aux is not None:
        print(aux.carro)
        aux = aux.prox


def retirar_carro(pilha, carro_procurado):
    retirados = []

    while pilha is not None:

        if pilha.carro == carro_procurado:
            print("\nCarro escolhido encontrado:", pilha.carro)

            pilha = pilha.prox

            return pilha, retirados

        print("Retirando:", pilha.carro)

        retirados.append(pilha.carro)

        pilha = pilha.prox

    print("\nCarro não encontrado.")

    return pilha, retirados


# Cadastrando os 20 carros
pilha = None

for i in range(1, 21):
    carro = "Carro " + str(i)
    pilha = push(pilha, carro)


print("===== CARROS NA GARAGEM =====")
listar(pilha)

numero = int(input("\nQual carro você deseja retirar? (1 a 20): "))

carro_procurado = "Carro " + str(numero)

pilha, retirados = retirar_carro(pilha, carro_procurado)

print("\n===== CARROS RETIRADOS =====")

if len(retirados) == 0:
    print("Nenhum carro precisou ser retirado antes.")
else:
    for carro in retirados:
        print(carro)

print("\n===== CARROS QUE PERMANECERAM =====")
listar(pilha)
