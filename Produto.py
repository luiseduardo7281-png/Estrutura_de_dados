class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def mostrar_informacao(self):
        print("Nome do Produto: ", self.nome)
        print("Preço do Produto: ", self.preco)
        print("Quantidade Disponível: ", self.quantidade)

controleXbox = Produto("Controle de Xbox", 66.66, 80)
controlePlay = Produto("Controle de PlayStation", 67.67, 150)
controleXbox.mostrar_informacao()
controlePlay.mostrar_informacao()
