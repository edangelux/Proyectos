#objetos en cierta medida es similar como un arreglo, te permite agrupar contenido de diferentes tipos de datos. Usualmente se accede a un elemento de un array por medio de su indice, en un objeto se accede por medio de una llave, en python se les conoce como diccionario

#creando diccionario

cancion = {
    'artista' : 'Metallica', #llave y valor
    'cancion' : 'Enter sadman',
    'lanzamiento' : 1992,
    'likes' : 3000
}

#acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

#mezclar un string
artista = cancion['artista']

print(f'estoy escuchando {artista}')

#agregar nuevos valores
cancion['playlist'] = 'heavy metal'

#cambiar valores
cancion['cancion'] = 'gola'
print(cancion)

#eliminar valores
del cancion['lanzamiento']
print(cancion)


#############################################################################################################diccionario vacio

jugador = {}
print(jugador)

#se coloca el dato
jugador['nombre'] = 'juan'
jugador['puntaje'] = 0
print(jugador)

#incrementando puntaje
jugador['puntaje'] = 100
print(jugador)

#iterar en el diccionario

for llave, valor in jugador.items():
    print(llave)
    print(valor)