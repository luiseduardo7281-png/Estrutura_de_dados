class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, valor):
        self.quantidade += valor


produto1 = Produto("Arroz", 25.00, 10)
produto2 = Produto("Feijão", 8.50, 20)

print("ANTES DA ATUALIZAÇÃO")
print("Produto:", produto1.nome)
print("Preço: R$", produto1.preco)
print("Quantidade:", produto1.quantidade)

print("\nProduto:", produto2.nome)
print("Preço: R$", produto2.preco)
print("Quantidade:", produto2.quantidade)

produto1.atualizar_estoque(5)
produto2.atualizar_estoque(10)

print("\nDEPOIS DA ATUALIZAÇÃO")
print("Produto:", produto1.nome)
print("Preço: R$", produto1.preco)
print("Quantidade:", produto1.quantidade)

print("\nProduto:", produto2.nome)
print("Preço: R$", produto2.preco)
print("Quantidade:", produto2.quantidade)