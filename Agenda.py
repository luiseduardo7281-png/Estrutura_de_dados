class Contato:
     def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
luis = Contato("Luis", "55 997221501", "Luis@gmail.com")
augusto = Contato("Augusto", "55 992288390", "Augusto@gmail.com")
leticia = Contato("Leticia", "55 999999999", "Leticia@gmail.com")

agenda = [luis, augusto, leticia]

for i in range(len(agenda)):
    print(agenda[i].nome)
    print(agenda[i].telefone)
    print(agenda[i].email)
    print("--------")