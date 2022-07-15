#podemos tener una lista hecha de listas
#tambien como los string podem os indexarlas y fraccionarla
#nos permiten metodos de manipularlas y analizarlas
#NO SON INMUTABLES, se pueden modificar y reorganizar
mi_lista1 = ['d','e','f']
mi_lista = ['a','b','c']
print(type(mi_lista))

resultado = len(mi_lista)
print(resultado)

resultado1 = mi_lista[0]
print(resultado1)

print(mi_lista + mi_lista1)

mi_lista[0] = 'alfa'
print(mi_lista)

mi_lista1.append('g')
print(mi_lista1)

mi_lista.pop()# si no lo especificas python asume que tiene que eliminar el ultimo dato de la lista
mi_lista1.pop(5)#eliminas el indice 5

mi_lista3 = ['b','c','r','l','h']
mi_lista3.sort()
mi_lista3.reverse()#lo ordena al reves
print(mi_lista3)



mi_lista4 = ['a','b','c','d','e']

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)