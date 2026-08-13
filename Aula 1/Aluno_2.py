class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / 3

    def verificar_aprovacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


aluno1 = Aluno("Pedro", [8, 7, 9])
aluno2 = Aluno("Lucas", [5, 6, 4])

print("Aluno:", aluno1.nome)
print("Média:", aluno1.calcular_media())
print("Resultado:", aluno1.verificar_aprovacao())

print()

print("Aluno:", aluno2.nome)
print("Média:", aluno2.calcular_media())
print("Resultado:", aluno2.verificar_aprovacao())
