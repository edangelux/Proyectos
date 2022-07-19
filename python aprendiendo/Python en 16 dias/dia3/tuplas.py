#es similar a las listas pero no son inmutables una vez que fue asignado no puede cambiarse
#se escribe igual que las listas pero se pone parentesis o nada en vez de corchete
#ocupan menos espacio(mas eficiencia)
#aprueba de daños

mi_tuple = (1,2,3,4)
print(type(mi_tuple))

mi_tuple1 = (1,2,(10,20,30),3,4)
print(mi_tuple1[2])
print(mi_tuple1[2][1])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1,2,3) #solo se puede con listas de mismos datos
x,y,z = t
print(x,y,z)

t1 = (1,2,3,1)
print(t1.count(1)) #imprime cuentas veces esta contado algo
print(t1.index(2)) #el valor dos en que indice se encuentra

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))


mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
