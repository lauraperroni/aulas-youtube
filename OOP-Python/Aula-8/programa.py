class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

    def imprimirNome(self):
        print(f'O nome do animal é: ', self.nome)
    
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miauu!"

class Passarinho(Animal):
    def fazer_som(self):
        return "Piu piu!"
    
# ------------------------------
    
cachorro = Cachorro("Bilu")
gato = Gato("Fofuxo")
passarinho = Passarinho("Pintinho Amarelinho")

print(cachorro.nome + " faz: " + cachorro.fazer_som())
print(gato.nome + " faz: " + gato.fazer_som())
print(passarinho.nome + " faz: " + passarinho.fazer_som())

cachorro.imprimirNome()
gato.imprimirNome()
passarinho.imprimirNome()

# ------------------------------

def fazer_barulho(animal):
    print(animal.nome + " faz: " + animal.fazer_som())

cachorro = Cachorro("Bilu")
gato = Gato("Fofuxo")
passarinho = Passarinho("Pintinho Amarelinho")

fazer_barulho(cachorro)
fazer_barulho(gato)
fazer_barulho(passarinho)