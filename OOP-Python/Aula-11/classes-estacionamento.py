class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True
    
    def sair_da_vaga(self):
        self.estacionado = False

# ==============================================
        
class Moto:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

# ==============================================
        
class Vaga:
    def __init__(self, identificador, tipo):
        self.id = identificador
        self.livre = True

        if tipo is not 'carro' and tipo is not 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')
        
        self.tipo = tipo
        self.placa = None