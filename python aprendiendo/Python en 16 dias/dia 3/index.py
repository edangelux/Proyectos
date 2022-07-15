#conocer el indice de un caracter
#conocer el caracter del indice

texto = 'hola'
texto.index('o')
resultado = texto[3]

texto1 = 'Que haces'
resultado1 = texto[2]
print(resultado1)

texto2 = '543210'
resultado2 = texto[-3]#al buscar un index negativo se puede, lee de derecha a izquierda
print(resultado2)

texto3 = 'que paso'
resultado3 = texto3.index('p')
print(resultado3)

texto4 = 'Como toshiba'
resultado4 = texto4.index('toshiba') #busca la palabra exacta
print(resultado4)

texto5 = 'Esto es una palabra'
resultado5 = texto5.index('a',12 ) #busca desde el margen de posicion de 12
print(resultado5)

texto6 = 'nueva tecnologia'
resultado6 = texto6.rindex('a') #rindex hace el inverso lee de derecha a izquierda
print(resultado6)


palabra = "ordenador"
resultado = palabra[4]
print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index('práctica')
print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex('práctica')
print(resultado)