class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / 3

aluno1 = Aluno("Ana", [8, 7, 9])
aluno2 = Aluno("Bruno", [6, 8, 7])
aluno3 = Aluno("Carlos", [9, 10, 8])

turma = [aluno1, aluno2, aluno3]

for aluno in turma:
    print("Nome:", aluno.nome)
    print("Média:", aluno.calcular_media())
    print()
