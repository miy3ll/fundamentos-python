tijeras = 1
piedra = 2
papel = 3

jugador1 = int(input("Jugador 1: Elige piedra (2), papel (3) o tijeras (1): "))
jugador2 = int(input("Jugador 2: Elige piedra (2), papel (3) o tijeras (1): "))
if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == tijeras and jugador2 == papel) or (jugador1 == piedra and jugador2 == tijeras) or (jugador1 == papel and jugador2 == piedra):
    print("Gana el jugador 1")
else:
    print("Gana el jugador 2")

