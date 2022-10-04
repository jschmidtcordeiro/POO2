from ave import Ave

class Canarinho(Ave):
    def __init__(self, tamanho_passo, altura_voo):
        super().__init__(tamanho_passo, altura_voo)
        
    def produzir_som(self, tipo_som):
        return super().produzir_som(tipo_som)
    
    def cantar(self):
        tipo_som = "PIU"
        som = self.produzir_som(tipo_som)
        return som