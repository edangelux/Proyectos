""" programacion orientada a objetos es una forma de escribir codigo que se considera de las mas efectivas 
cuando defines una clase lo que haces en programacion orientada a objetos describes comportamineto y forme del objeto 

objeto de la forma de referirse a la infomracion creada por una clase, cada instancia de la clase tendra la misma forma pero diferente informacion


class Cliente:
    #resto de la clase 
    cliente = Cliente() 
    
    
    
    TERMINOLOGIA: 1)instancia: el objeto que es creado al llamar una clase 
                  2)atributo de la clase: es una propiedad que tendran todos los objetos creados con nuestras clases
                  3)metodo: es una funcion que existe dentro de una clase"""


"""                                     ABSTRACCION
son los datos necesarios de una clase, si elaboras un menu de un restaurant es necesario el nombre del platillo, descripcion y precio, otros datos como el color favorito del chef no es necesario"""

"""                                     ENCAPSULAMIENTO
permite restringir o ocultar acceso  de los datos sobre la misma clase """

"""                                       HERENCIA 
puedes crear una clase que sea hijo o una copia, al heredar una clase tendra los metodos y atributos de la clsae de padre a hijo y modificarlo en casos que sea necesario  """

"""                                      POLIMORFISMO
Es la habilidad de tener diferentes comportamientos basados en que subclase se esta utilizando, relacionado estrechamente con la herencia  """



class Restaurant:

#constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.__precio = precio #default: publica, agregandole _ es PROTECTED ejemplo: _hola
           # existe PRIVATE que con el es doble guin bajo ejemplo: __hola 
    
    """ def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo """

    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.__precio}')

#getters y setters: get = obtiene un valor, set = agrega un valor 
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio

# clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, piscina):
        super().__init__(nombre, categoria, precio)
        self.piscina = piscina #polimorfismo

    #reescribir un metodo(debe de llamarse igual)
    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.__precio}, piscina:{self.piscina}')


    #agregar un metodo que solo existe en hotal(polimorfismo)
    def get_piscina(self):
        return self.piscina

hotel = Hotel('Hotel lokera', '4 estrellas', 200, 'si')
hotel.mostrar_informacion()
piscina  = Hotel.get_piscina()



#instanciar la clase 
restaurant = Restaurant('Pizzeria lokito', 'Comida Italiana', 50)
""" restaurant.agregar_restaurant('Pizzeria lokito') """

restaurant.mostrar_informacion()
restaurant.set_precio(30)
precio = restaurant.get_precio()
print(precio)


restaurant2 = Restaurant('Hamburgesa payaso', 'Comida Rapida', 20)
""" restaurant2.agregar_restaurant('Hamburgesa payaso') """


restaurant2.mostrar_informacion()
restaurant2.get_precio(40)
restaurant2.get_precio() 


#mostrar informacion
print(f'nombres restaurant: {restaurant.nombre}')
print(f'nombres restaurant: {restaurant2.nombre}')


