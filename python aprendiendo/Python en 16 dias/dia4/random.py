#numero entero aleatorio = randint
#pertenece a una librerria llamada random pero los metodos de random no estan cargados directamente
#tenemos que importar los metods de esta manera = from random import randint

#randint()
#uniform() da un valor aleatorio decimal
#random() aleatorio decimal de 0 y  1
#choice() metodo random pero seleccionando en especifico una lista o cadena
#shuffle() mezclar una lista

from random  import *  

aleatorio = randint(1,100)
print(aleatorio)

aleatorio1 = round(uniform(1,5),2)
print(aleatorio1)

aleatorio2 = random()
print(aleatorio2)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio3 = choice(colores)
print(aleatorio3)

cartas = list(range(1,15))

shuffle(cartas)
print(cartas)



aleatorio4 = randint(1,10)


aleatorio5 = random()
print(aleatorio5)


from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)