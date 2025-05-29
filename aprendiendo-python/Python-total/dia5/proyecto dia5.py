""" el programa va a elegir una plabara secreta y el juegador se le imprimira una serie de guiones que es la cantidad de letras que hay en la plabra secreta
el jugador por turno tiene que elegir una letra y si la letra se encuentra en la palabra secreta se mostrara en que posicion esta la letra per si el juegador no coloca una letra
que hay en la palabra secreta entonces perdera una vida tienen 6 vidas en total y cada vez que pierda una se le dira y si adivina todo se le dira que gano
y si pierde las vidas se le dira que perdio

usaremos choice y funciones"""


from random import *

def seleccionar_palabra(): #seleccionara una palabra al alazar de estas
    palabras = ["hola", "python", "juego", "programacion", "palabra"]
    return choice(palabras)

def inicializar_juego(palabra): #inicializamos variables del juego para mas adelante
    letras_adivinadas = ["_"] * len(palabra)
    vidas = 6
    letras_intentadas = []
    return letras_adivinadas, vidas, letras_intentadas

def mostrar_estado(letras_adivinadas, vidas, letras_intentadas): #mostrar el comienzo del juego 
    print("\nPalabra: " + " ".join(letras_adivinadas))
    print("vidas restantes:", vidas)
    print("letras intentadas:", " ".join(letras_intentadas))
    
def procesar_intento(letra, palabra, letras_adivinadas, letras_intentadas): #procesa el intento del jugador
    letras_intentadas.append(letra)
    acierto = False
    for i in range(len(palabra)):
        if palabra[i] == letra:
            letras_adivinadas[i] = letra
            acierto = True
    return acierto
    
def jugar_ahorcado(): #funcion principal para el flujo del juego
    palabra = seleccionar_palabra()
    letras_adivinadas, vidas, letras_intentadas = inicializar_juego(palabra)
    
    print("juguemos al AHORCADO")
    print("la palabra tiene", len(palabra), "letras")
    
    while True:
        mostrar_estado(letras_adivinadas, vidas, letras_adivinadas)
        
        if "_" not in letras_adivinadas: #si en dado caso el jugador gana
            print("FELICIDADES has GANADO")
            print("\n la palabra es: ", palabra)
            break
        
        if vidas <=0: # si en dado caso el juegador pierde
            print("PERDISTE  la palabra era: ", palabra)
            break
        
        letra = input("ingrese una letra: ").lower() # todas las letras se toman en minusculas
        
        if len(letra) != 1 or not letra.isalpha(): #validacion de letra
            print("Por favor ingresa solo una letra valida")
            continue
        
        if letra in letras_intentadas:  # Validación de repetidas
            print("Ya intentaste esa letra")
            continue
        
        acierto = procesar_intento(letra, palabra, letras_adivinadas, letras_intentadas)
        
        if not acierto: #cuando pierda cada oportunidad
            vidas -=1
            print("letra incorrecta. Pierdes una vida")

jugar_ahorcado() #comienza la mierda esta