class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
  
    def total_estoque(self):
        preco_estoque = self.preco*self.quantidade
        print("O preço total do estoque é: R$", preco_estoque)
        
    def mostrar_informacao(self):
        print("Nome do Produto: ", self.nome)
        print("Preço do Produto: R$", self.preco)
        print("Quantidade Disponível: ", self.quantidade)
    
controleXbox = Produto("Controle de Xbox", 66.66, 80)
controlePlay = Produto("Controle de PlayStation", 67.67, 150)
controleXbox.mostrar_informacao()
controleXbox.total_estoque()
controlePlay.mostrar_informacao()
controlePlay.total_estoque()
