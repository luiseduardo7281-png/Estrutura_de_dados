class Aluno:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.quantidade = 0
        self.situacao = True
        
    def alterar_disciplinas(self, quantidade):
        self.quantidade = quantidade 
        
    def mostrar_quantidade_disciplinas(self):
        print("Quantidade de disciplinas: ", self.quantidade)
        
    def alterar_situacao(self):
        if self.situacao == True:
            self.situacao = False
            
        else:
            self.situacao = True
            
    def mostrar_situacao(self):
        print("Nome: ", self.nome)
        print("Situação: ", self.situacao)
        self.mostrar_quantidade_disciplinas()    
        
luis = Aluno("Luis Eduardo", 18, "Recanto Maestro")
luis.mostrar_situacao()
luis.alterar_situacao()
luis.alterar_disciplinas(10)
luis.mostrar_situacao()

print()
luiz = Aluno("Luiz Alawi", 18, "TecnoAMF")
luiz.mostrar_situacao()