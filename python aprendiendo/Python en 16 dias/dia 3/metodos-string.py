#upper() mayusculas
#lower() minusculas
#split() separarlo en partes
#join() unir lo separado
#find() encontrar un sub-string
#replace() reemplazar un sub-string

texto = 'hola texto'
resultado = texto.upper()
resultado1 = texto.lower()
resultado2 = texto.split()
resultado3 = texto.split('t') #cada vez que llegue a una t corta
resultado4 = texto.find('t') #es casi igual que index pero en este casi si no lo encuentra da un -1
resultado5 = texto.replace('texto','escrito')
resultado6 = texto.replace('o','x') #todas las letras de o cambian a x

print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)

a = 'hola'
b = 'como'
c = 'estas'
d = ' '.join([a,b,c]) #lo que hace aqui al incio es dar un espacio y luego unir los 3 string
print(d)


frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
mayusculas = frase.upper()
print(mayusculas)

lista_palabras = ["La","legibilidad","cuenta."]
unir = " ".join(lista_palabras)
print(unir)

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
cambiar = frase.replace('difícil', 'fácil').replace('mala','buena')
print(cambiar)
