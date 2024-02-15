from abc import ABC, abstractmethod

# --------------------------------------------
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def fazer_som(self):
        pass
# --------------------------------------------
    
class Cachorro(Animal):
    def fazer_som(self):
        return "au au!"
    
class Gato(Animal):
    def fazer_som(self):
        return "miau!"
    
# --------------------------------------------

cachorro = Cachorro("bolt")
gato = Gato("mittens")

print(cachorro.fazer_som())
print(gato.fazer_som())