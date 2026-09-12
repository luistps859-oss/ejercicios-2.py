import random

numero_secreto = random.randint(1, 100)
intento = 0  # empezamos en 0 para que el while entre la primera vez

while intento != numero_secreto:
    intento = float(input("Adivina el número (1-100): "))
    
    if intento < numero_secreto:
        print("el numero secreto es mas alto")
    elif intento > numero_secreto:
        print("el numero secreto es mas bajo")

print("¡Felicidades, adivinaste el número!")
