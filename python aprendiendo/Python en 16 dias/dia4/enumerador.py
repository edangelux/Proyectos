lista = ['a','b','c']

for indice,item in enumerate(lista):
    print(indice,item)

lista1 = ['d','e','f']

mis_tuples = list(enumerate(lista1))
print(mis_tuples)



lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


texto = "Python"

lista_indices = list(enumerate(texto))
print(lista_indices)



lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in lista_nombres:
    if nombre.startswith('M'):
        indice=int(lista_nombres.index(nombre))
        print(indice)