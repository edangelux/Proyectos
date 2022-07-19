#while = mientras que

monedas = 5

while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas -= 1
else:
    print('no tengo mas dinero')


respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres segui? S/N ')
else:
    print('gracias')


nombre = input('tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)


nombre1 = input('tu nombre: ')

for letra1 in nombre1:
    if letra1 == 'r':
        continue #se va a saltar la r
    print(letra1)




numero = 10

while numero >= 0:
    print(numero)
    numero -= 1



numero = 50


while numero >=0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
        continue


lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for i in lista_numeros:
    if i < 0:
        break
    else:
        print(i)