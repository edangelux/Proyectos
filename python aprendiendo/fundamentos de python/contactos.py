"""                                CRUD
            c = Create, r = Read, u = Update d = Delete """


from ast import Try
import os #libreria diseñada para manejo de archivos

CARPETA = 'agenda/' #carpeta de contacto
EXTENSION = '.txt' #extension de archivos

#class de contactos
class Contacto:
    def __init__(self, nombre, celular, categoria):
        self.nombre = nombre
        self.celular = celular 
        self.categoria = categoria


def app():

    crear_directorio() #revisa si la carpeta existe
    menu()#mostrar menu

    preguntar = True
    while preguntar:
        opcion = input('seleccione una opcion \n')
        opcion = int(opcion)

        #opciones
        if opcion == 1:
            print('AGREGAR CONTACTO')
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('EDITAR CONTACTO')
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print('VER CONTACTO')
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            print('BUSCAR CONTACTO')
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            print('ELIMINAR CONTACTO')
            eliminar_contacto()
            preguntar = False
        else:
            print('OPCION NO VALIDA, INTENTE DE NUEVO')


 #agregamos el contacto
def agregar_contacto():
    #pedimos los datos
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto: ')
    celular_contacto = input('Agrega el numero: ')
    categoria_contacto = input('Coloca la categoria del contacto: ')

    #instanciar la clase
    contacto = Contacto(nombre_contacto, celular_contacto, categoria_contacto)

    #revisamos si el archivo existe antes de generarlo
    existe = existe_contacto(nombre_contacto)

    

    if not existe:
        #abrimos carpeta y anexamos los datos 
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            archivo.write('Nombre: ' + contacto.nombre+ '\n')
            archivo.write('Nombre: ' + contacto.celular+ '\n')
            archivo.write('Nombre: ' + contacto.categoria + '\r\n')

        #decirle al usuario que fue creado
        print('\r\n CONTACTO CREADO CORRECTAMENTE \r\n')
    else:
        print('Disculpa ese contacto ya existe \n')
    
    #reiniciar app
    app()

#editamos contacto
def editar_contacto():
    print('Escriba el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \n')

    #revisamos si el archivo existe antes de editar
    existe = existe_contacto(nombre_anterior)

    if existe:
        print('Puedes continuar editando')
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #editar los campos
            nombre_contacto = input('Agrega el nuevo nombre: ')
            celular_contacto = input('Agrega el nuevo numero: ')
            categoria_contacto = input('Agrega la nueva categoria: ')

            #instanciar la clase
            contacto = Contacto(nombre_contacto, celular_contacto, categoria_contacto)

            #escribir en el documento
            archivo.write('Nombre: ' + contacto.nombre+ '\n')
            archivo.write('Celular: ' + contacto.celular + '\n')
            archivo.write('Categoria: ' + contacto.categoria + '\n')

        #renombrar archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        #mensaje de confirmacion
        print('\r\n Contacto agregado correctamente \r\n')
    else:
        print('Disculpe pero ese contacto no existe')
    
    #reiniciar la app
    app()

def mostrar_contacto():
    print('SE MOSTRATA TODOS LOS CONTACTOS \n')
    archivos = os.listdir(CARPETA) #llamamos una lista de los contactos
    archivos_txt = [i for i in archivos if i.endswith (EXTENSION)] #especificamos que sean unicamente txt

    for archivo in archivos_txt: #iteramos dentro de ella para imprimir
        with open(CARPETA + archivo) as contacto:
            for agenda in contacto:
                print(agenda.rstrip()) #imprimos la agenda de contacto
            print('\n')

    #reiniciar app
    app()

def buscar_contacto():
    print('Busque el contacto exacto \n')
    nombre = input('Coloque el nombre del contacto que desea buscar: ')

    try:
        with open( CARPETA + nombre + EXTENSION) as contacto:
            print('Informacion del contacto: ')
            for agenda in contacto:
                print(agenda.rstrip())
            print('\n')
    except IOError:
        print('El contacto no existe\n')
        print(IOError)

    #reinciar app
    app()

def eliminar_contacto():
    print('Desea eliminar contacto')
    eliminar = input('Seleccione el contacto que desea eliminar: ')

    try:
        os.remove(CARPETA + eliminar + EXTENSION)
        print('Eliminado Correctamente \n ')
    except:
        print('No existe este contacto')
    #reiniciar app
    app()
    
def menu():
    print('Elija la opcion de lo que quiera hacer')
    print('1) Agregar contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def existe_contacto(nombre):
     #revisamos si el archivo existe antes de editar
    return os.path.isfile(CARPETA + nombre + EXTENSION) 

app()