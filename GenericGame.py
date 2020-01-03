from Baraja import Baraja
from Jugador import Jugador
from Constantes import Constantes


#Se crea la baraja
baraja=Baraja()

#Se muestra la baraja
baraja.mostrar()

#Se crean los jugadores
jugadores=[]
for i in range(	Constantes.NUMERO_JUGADORES ):
	nombre_jugador="Jugador"+repr(i+1)
	jugadores.append(Jugador(nombre_jugador)) 

#Se reparten las cartas a los jugadores
for i in range(Constantes.CARTAS_POR_JUGADOR):
	for j in range(	Constantes.NUMERO_JUGADORES ):
		jugadores[j].recibirCarta(baraja) 
	
#Se muestran las cartas de los jugadores
for j in range(	Constantes.NUMERO_JUGADORES ):
	jugadores[j].mostrar()
	
#Se muestran las cartas que quedan
baraja.mostrar()