""" hacer un analizador de texto
pedir a un usuario que ingrese un texto
y que el usuario ingrese 3 letras 
dandole la informacion de cuantas veces aparece esa letra
cuantas palabras hay en total 
cual es la primera letra y la ultima
texto invertido
y si dice que dice python en el texto """

texto = input("dame el texto que quieres analizar:\n").lower()
print(type(texto))

letras = input("dame 3 letras que quieres analizar:\n").lower().split()


#contador de letras
contar_letras = {letras[0]: texto.count(letras[0]), letras[1]: texto.count(letras[1]), letras[2]: texto.count(letras[2])}
print(contar_letras)

#contar palabras
contar_longitud = texto.split()
longitud = print(len(contar_longitud))

#primera y ultima letra
primer_letra = print(texto[0])
ultima_letra = print(texto[-1])

#texto invertido
texto_invertido = print(texto[::-1])

#si sale "python" en el texto"
texto_texto = print("python" in texto)