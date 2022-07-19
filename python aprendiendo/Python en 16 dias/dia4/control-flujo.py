#es el gen de la automatizacion en un codigo

#if = si
#elif = si no ocurre lo otro tal vez esto si
#else = si no ocurre ya nada de lo anterior

if 10 > 9:
    print('es correcto')

if 5 == 2:
    print('es correcto')
else:
    print('no es correcto')

mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('es un perro')
elif mascota == 'pez':
    print('es un pez')
else:
    print('no se')


edad = 16
calificacion = 10

if edad < 18:
    print('eres adolescente')
    if calificacion >= 6:
        print('aprobaste')
    else:
        print('desaprobo')
else:
    print('eres adulto')



num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 < num1:
    print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")




edad = 16
tiene_licencia = False

if edad >= 18:
    print("Puedes conducir")

elif edad <= 17:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

elif tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")


habla_ingles = True
sabe_python = False

if habla_ingles and (sabe_python):
    print("Cumples con los requisitos para postularte")

elif habla_ingles and sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

elif not(habla_ingles):
    print("Para postularte, necesitas tener conocimientos de inglés")

elif not sabe_python:
    print("Para postularte, necesitas saber programar en Python")