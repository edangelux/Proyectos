nombre = input('cual es tu nombre')

print(f'hola {nombre}')
############################################################################################################

#leer datos que seran numeros
edad = input('cual es tu edad?')
#convertir edad(string) a int
edad = int(edad)

if edad >= 16:
    print('ya puedes votar')
else:
    print('aun no puedes')

############################################################################################################
pregunta = 'agregar un numero y vere si es par o no \r\n'
pregunta += '(escribe "cerrar" para salir del juego)\r\n'

preguntar = True

while preguntar:

    #mezclar con operadores
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        
        if numero % 2 == 0:
            print(f'el numero {numero} es par')
        else:
            print(f'el numero {numero} es impar')

############################################################################################################

numero = 0

while numero <= 10:
    print(numero)
    numero += 1 #incrementando para evitar loop infiinito

#if dentro de un while

while numero <= 10:
    if numero == 5:
        print('CINCO')
    else:
        print(numero)
    numero += 1