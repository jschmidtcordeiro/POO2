from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self, volume_som=3, tamanho_passo=3):
        super().__init__(volume_som, tamanho_passo)
        
    def produzir_som(self, tipo_som):
        return super().produzir_som(tipo_som)

    def latir(self):
        tipo_som = "AU"
        som = self.produzir_som(tipo_som)
        return som