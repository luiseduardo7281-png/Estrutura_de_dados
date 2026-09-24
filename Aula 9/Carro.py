class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")


carro = Carro("Toyota", "Corolla", 2024)

print("Marca:", carro.marca)
print("Modelo:", carro.modelo)
print("Ano:", carro.ano)

carro.ligar()
carro.desligar()
