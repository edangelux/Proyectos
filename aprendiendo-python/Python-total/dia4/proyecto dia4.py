""" haremos un programa que le pregunte el nombre a la persona
y hacer que el programa le pregunte a el usuario un numero del 1 al 100
de manera random
si elige un numero menor al numero random, el programa le dira que es menor
si elige un numero mayor al numero random, el programa le dira que es mayor
si elige un numero igual al numero random, el programa le dira que es igual
y si acierta se le dira que gano, de 8 intentos el programa para adivinar """

from random import *
nombre = input("cual es tu nombre: ")
print("hola " + nombre + " voy a jugar contigo a adivinar un numero del 1 al 100")

intentos = 8
numero_secreto = randint(1,100)

while intentos > 0:
    print("\n adivina el numero que estoy pensando, tienes ", intentos, "intentos")
    numero_usuario = int(input("ingresa un numero del 1 al 100: "))
    if numero_usuario < numero_secreto:
        print("El numero que ingresaste es menor")
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
    elif numero_usuario > numero_secreto:
        print("El numero que ingresaste es mayor")
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
    else:
        print(f"Ganaste El numero era {numero_secreto}. Lo lograste en {8 - intentos} intentos")
        break
else:
    print(f"\nPerdiste. El numero secreto era {numero_secreto}")