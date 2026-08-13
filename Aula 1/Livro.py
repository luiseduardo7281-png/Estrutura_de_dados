class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def verificar_tamanho(self):
        if self.paginas <= 100:
            return "curto"
        else:
            return "longo"


livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)
livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 863)

print("Livro:", livro1.titulo)
print("Autor:", livro1.autor)
print("O livro é:", livro1.verificar_tamanho())

print()

print("Livro:", livro2.titulo)
print("Autor:", livro2.autor)
print("O livro é:", livro2.verificar_tamanho())
