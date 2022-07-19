#hacer que el usuario coloque un texto
#pedirle 3 letras que esten en el texto
#mostrar cuantas veces aparece cada letra (pasar las letras en minusculas)
#cuantas palabras hay en total
#decir cual es la primera letra y la ultima del texto
#mostrar el texto en inverso
#decir si la palabra python se encuetra en el texto

texto = input('ingrese el texto: ')

#hacer minisculas por si acaso se me olvida luego
texto = texto.lower()

#pedir letras del usuario
print('\n')
print('ingreseme 3 letras que este en el texto chele')
letra1 = input('letra 1: ')
letra2 = input('letra 2: ')
letra3 = input('letra 3: ')

#creo que aqui lo hace minusculas
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

#contar cuantas veces hay en cada palabra pues

#convierto en tupla el texto
tupla = tuple(texto)
print('\n')
print('cuantas veces aparece las letras en el texto')
print(f'la letra {letra1} aparece {tupla.count(letra1)} en tu fucking texto')
print(f'la letra {letra2} aparece {tupla.count(letra2)} en tu fucking texto')
print(f'la letra {letra3} aparece {tupla.count(letra3)} en tu fucking texto')

#cuantas letras hay en total
print('\n')
print('cuantas letras hay en total en el texto')
print(len(tupla))

#primera y ultima letra en el textp
print(f'tu primera letra es {tupla[0]}')
print(f'tu ultima letra es {tupla[-1]}')

#mostrar texto en inverso
lista=list(texto)
lista.reverse()
nuevo="".join(lista)
print(f'El texto invertido es: {nuevo}')

#esta python en el texto
print('veremos si esta python en el texto')
if ('python' in texto):
    print('si aparece en el texto')
else:
    print('no ta la palabra en texto')


"""    print('\n')
    invertido = str(tupla)
    invertido = invertido[::-1]
    print(invertido)"""