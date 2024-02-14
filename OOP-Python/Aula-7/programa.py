class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
    
    def imprimirPet(self):
        print(f'Nome do pet: ', self.nome)
        print(f'Peso do pet: ', self.peso)

    def alimentarPet(self, comida):
        self.peso + comida
#----------------------------------------------
        
class Abrigo:
    __catalogo = []

    def adicionarPet(self, pet):
        self.__catalogo.append(pet)
    
    def imprimirAbrigo(self):
        print('Pets no abrigo:')
        print('---------------')

        for pet in self.__catalogo:
            pet.imprimirPet()
            print('---------------')

#----------------------------------------------

abrigo = Abrigo()

pet = Pet('Jujuba', 10)
abrigo.adicionarPet(pet)

pet = Pet('Carlinhos', 100)
abrigo.adicionarPet(pet)


abrigo.catalogo = []
abrigo.imprimirAbrigo()