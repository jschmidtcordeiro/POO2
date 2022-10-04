from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(volume_som=2, tamanho_passo=2)
        
    def produzir_som(self, tipo_som):
        return super().produzir_som(tipo_som)
    
    def miar(self):
        tipo_som = "MIAU"
        som = self.produzir_som(tipo_som)
        return som