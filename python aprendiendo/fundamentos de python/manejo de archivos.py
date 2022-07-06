def app():
    #crear archivo
    archivo = open('archivo.txt', 'w') #w archivo de escritura, si no existe lo crea 

    #generar numeros en archivos
    for i in range(1, 30):
        archivo.write('esta es la linea: ' + str(i) + "\n")

  


def terminal():
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip()) #remueve los saltos de linea: rstrip()


app()