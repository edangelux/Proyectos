"""string (str) = 'hola' 'como estas'
integer(int) = 10, 20, -10
floating(float) = 10.4, 10.45, 20.05
listas (lst) = ["sal", 1, -3.4, "hola"] funciona con orden del 0 - maximo
diccionario (dic) = {'color':'azul','categoria':'arte'} funciona mas para programacion de objetos
tuples (tup) = ('lunes','martes','miercoles') su orden no se cambia
sets (set) = {'a','b','c'} son unicos he inrepetibles
booleano(bool) = True,False  es cuando la condicion es verdadero o falso"""


#conversiones de tipos de datos

#se llama casting y existen dos tipos de casting
#implicita: es cuando el programa realiza la conversion de manera automatica de otro tipo de dato
#explicita: pedir al programa que comvierta el dato a otro tipo de dato de manera manual

#implicito
num1 = 20
num2 = 30.5

num1 = num1 + num2
print(type(num1))
print(type(num2))

#explicito
num3 = 3.5
print(type(num3))

num4 = int(num3)
print(type(num4))

num1 = 7.5
num2 = int(num1)
print(type(num2))

num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))