from classes_estacionamento import *
from random import randint


carros = []

for i in range(10):
    placa = randint(1000, 9999)
    carros.append(Carro(placa))

motos = []

for i in range(20):
    placa = randint(1000, 9999)
    motos.append(Moto(placa))


estacionamento = Estacionamento(5, 5)
print(estacionamento)

for i in range(4):
   estacionamento.estacionar_carro(carros[i]) 

print(estacionamento)

estacionamento.estacionar_carro(carros[4])
print(estacionamento)

estacionamento.estacionar_moto(motos[6])
print(estacionamento)

