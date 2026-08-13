class Aluno:
    def __init__(self, nome, frequencia, media):
        self.nome = nome
        self.frequencia = frequencia
        self.media = media
    
    def mostrar_situacao(self):
        print("Nome: ", self.nome)
        print("Frequencia: ", self.frequencia)
        print("Media Geral: ", self.media)

Joao = Aluno("Joao", 76, 7.8)
Joao.mostrar_situacao()
Maria = Aluno("Maria", 80, 8.5)
Maria.mostrar_situacao()
