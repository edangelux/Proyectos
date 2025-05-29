""" Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma """
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma += numero
    return suma
    
lista_numeros = [150, -50, 2500, 500, 1200, 800]        
print(suma_menores(lista_numeros))  # imprime 3800