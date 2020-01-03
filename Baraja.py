import random
from random import shuffle
from Carta import Carta


def NUMEROS(): return [ "As", "2", "3", "4", "5", "6", "7", "Sota", "Caballo", "Rey" ]
def PALOS(): return [ "Oros", "Copas", "Espadas", "Bastos" ]

class Baraja:

    def __init__( self ):
        self.contents = []
        self.contents = [ Carta( numero, palo ) for numero in NUMEROS() for palo in PALOS() ]
        random.shuffle( self.contents )
    
    def mostrar(self):
        print ("\nHay ",len(self.contents), " cartas")
        for i in range(len(self.contents)):
            print (i+1,":",self.contents[i])
    
    