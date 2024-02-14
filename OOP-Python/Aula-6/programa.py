
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        print(f'{self.nome} foi criado.')
    
    def __del__(self):
        print(f'{self.nome} foi destruído.')

pessoa1 = Pessoa("Laura")
pessoa2 = Pessoa("Carlo")

del pessoa2

print(pessoa1.nome)