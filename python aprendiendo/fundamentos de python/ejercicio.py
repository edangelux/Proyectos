playlist = {} #diccionario vacio\
playlist['canciones'] = [] #lista vacia de canciones



#funcion principal
def app():
    
    #agregar playlist
    agregar_playlist = True

    while agregar_playlist:

        nombre_playlist = input('como deseas nombrar la playlist?\r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #ya tenemos nombre desactivar true
            agregar_playlist = False

            #mandar a llamar agregar cacniones
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        #preguntar al usuario que cancion agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'agrega canciones para la playlist{nombre_playlist}:\r\n'
        pregunta += 'escribe "x" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == "x":
            #dejar de agregar canciones
            agregar_cancion = False

            # mostrar resumen de la playlist
            resumen()
        else:
            #agregar las canciones a la playlist
            playlist['canciones'].append(cancion)


def resumen():
    nombre_playlist = playlist['nombre']

    print(f'playlist: {nombre_playlist}\r\n')
    print('canciones:\r\n')

    for cancion in playlist['canciones']:
        print(cancion)
app()