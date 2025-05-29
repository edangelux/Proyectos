""" Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado. """

def cantidad_atributos(**kwargs):
    return len(kwargs)

print(cantidad_atributos(x=10, y=20))