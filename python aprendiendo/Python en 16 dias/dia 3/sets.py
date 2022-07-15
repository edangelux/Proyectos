#son una coleecion de elementos igual que las listas pero con algunas diferencias
#se pueden declarar de dos maneras usando 'set' o usando llave sin usar 'set'
# no estan ordenados por indices
#sus elementos no son mutables

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))

mi_set1 = set((1,2,3,4,5,5,6,7(6,3,2,3))) #se puede hacer esto con tupla por que la tupla es inmutable como el set
print(mi_set1)

mi_set2 = (1,2,3)
mi_set3 = (3,4,5)
set = mi_set2.union(mi_set3)
print(set)

mi_set2.add(5)
print(mi_set2)

mi_set2.remove(1)
print(mi_set2)

mi_set2.discard(7) #si no existe para eliminarlo unicamente continua el programa
print(mi_set2)

mi_set2.pop()
print(mi_set2)

mi_set2.clear()
print(mi_set2)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.remove('Axel')

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add('Damián')