""" Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta. """

def cantidad_pares(lista_numeros):
    pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
    return pares

lista_numeros = [1, 2, 3, 4, 5, 6, 7]
print(cantidad_pares(lista_numeros))  # Salida: 3