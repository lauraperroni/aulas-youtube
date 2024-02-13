class Televisao:
    def __init__(self):
        self.canal = 1
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99
        self.ligada = False
    # ---------------------------------------
    def ligar(self):
        self.ligada = True
    # ---------------------------------------
    def desligar(self):
        self.ligada = False
    # ---------------------------------------
    def mudar_canal_para_cima(self):

        if not self.ligada:
            return
        
        if self.canal < self.canal_max:
            self.canal += 1
    # ---------------------------------------
    def mudar_canal_para_baixo(self):

        if not self.ligada:
            return
        
        if self.canal > self.canal_min:
            self.canal -= 1
    # ---------------------------------------
    def reduzir_volume(self):

        if not self.ligada:
            return

        if self.volume > self.volume_min:
            self.volume -= 10
    # ---------------------------------------
    def aumentar_volume(self):

        if not self.ligada:
            return
    
        if self.volume < self.volume_max:
            self.volume += 10

    # ---------------------------------------
    def __str__(self) -> str:
        return f'Televisão - Está Ligada = {self.ligada} - Canal: {self.canal} - Volume: {self.volume}'

# -----------------------------------------------------
    
minha_tv = Televisao()

print(minha_tv)