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

class Restaurant:

#constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.precio = precio
    
    """ def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo """

    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.precio}')

#instanciar la clase 
restaurant = Restaurant('Pizzeria lokito', 'Comida Italiana', 50)
""" restaurant.agregar_restaurant('Pizzeria lokito') """
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Hamburgesa payaso', 'Comida Rapida', 20)
""" restaurant2.agregar_restaurant('Hamburgesa payaso') """
restaurant.mostrar_informacion()


#mostrar informacion
print(f'nombres restaurant: {restaurant.nombre}')
print(f'nombres restaurant: {restaurant2.nombre}')


