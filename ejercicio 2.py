import random

opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

usuario = input("Elige piedra, papel o tijera: ")

print("La computadora eligió:", computadora)

if usuario == computadora:
    print("¡Empate!")
elif (usuario == "piedra" and computadora == "tijera") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("¡Ganó la computadora!")