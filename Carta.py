class Carta: 
    def __init__(self, numero, palo):
        self.numero=numero
        self.palo=palo
        
    def __str__(self):
        return self.numero + " de " + self.palo