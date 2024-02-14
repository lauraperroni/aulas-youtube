class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 300

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print('Carro foi ligado com sucesso.')
        else:
            print('O carro já está ligado!')

    def desliga(self):
        if not self.ligado:
            print('O carro já está desligado!')
        else:
            self.ligado = False

    def acelera(self):
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10
            print(f'Sua velocidade agora é de ', self.velocidade, 'Km/h')
        else:
            print('Você está na velocidade máxima!')
    
    def desacelera(self):
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
            print(f'Sua velocidade agora é de ', self.velocidade, 'Km/h')
        else:
            print('O carro está parado!')


#------------------------------------
        
carro = Carro('vermelho', 'honda civic')

carro.liga()
carro.acelera()
carro.desacelera()