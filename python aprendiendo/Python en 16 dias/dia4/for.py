lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'letra {numero_letra}: {letra}')

lista1 = ['pablo','laura','federico','luis','julia']

for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)


numeros = [1,2,3,4,5,6]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

palabra = 'python'
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2':'b', 'clave3':'c'}

for item in dic.items():
    print(item)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print('Hola '+ nombre)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for suma_numero in lista_numeros:
    suma_numeros = suma_numeros + suma_numero
    print(suma_numeros)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for i in lista_numeros:
    if i %2 == 0:
        suma_pares = suma_pares + i
    elif i %2 == 1:
        suma_impares = suma_impares + i

print(suma_impares)
print(suma_pares)
