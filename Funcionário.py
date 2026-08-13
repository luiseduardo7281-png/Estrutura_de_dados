class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            return self.salario * 0.10
        else:
            return self.salario * 0.05


funcionario1 = Funcionario("Carlos", 5000, "Gerente")
funcionario2 = Funcionario("João", 3000, "Vendedor")

salario1 = funcionario1.salario + funcionario1.calcular_bonus()
salario2 = funcionario2.salario + funcionario2.calcular_bonus()

print("Funcionário:", funcionario1.nome)
print("Cargo:", funcionario1.cargo)
print("Salário com bônus: R$", salario1)

print()

print("Funcionário:", funcionario2.nome)
print("Cargo:", funcionario2.cargo)
print("Salário com bônus: R$", salario2)