from Baraja import Baraja
from Constantes import Constantes

class Jugador:
    
     def __init__(self, nombre):
        self.contents = [] 
        self.nombre = nombre
        
     def recibirCarta(self, baraja):
         self.contents.append(baraja.contents.pop())
         
     def mostrar(self):
         print ("\n"+self.nombre+" tiene estas cartas:")    
         for i in range(Constantes.CARTAS_POR_JUGADOR):
             print(i+1,self.contents[i])