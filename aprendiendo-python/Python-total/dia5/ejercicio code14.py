""" Práctica sobre Interacción entre Funciones 2
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo. """

def reducir_lista(lista):
    lista_sin_duplicado = []
    for numero in lista:
        if numero not in lista_sin_duplicado:
            lista_sin_duplicado.append(numero)
    if lista_sin_duplicado:
        lista_sin_duplicado.remove(max(lista_sin_duplicado))
    return lista_sin_duplicado

def promedio(lista_reducida):
    return sum(lista_reducida) / len(lista_reducida)


lista_numeros = [1,2,15,7,2]
lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)
print(promedio(lista_numeros))