#una caja, un espacio para almacenar algo puede cambiar

nombre = 'eddy'
print(nombre)

 #cambia el valor de la variable
nombre = 'elias'
print(nombre)

edad_nacido = 17
edad_muerto = 3
print(edad_nacido + edad_muerto)

nombre_usuario = input('Coloque su nombre: ')
print(nombre_usuario)

saludo = 'hola '
lenguaje = 'python'
saludando = saludo + lenguaje
print(saludando)

nombre = 'Tony Soprano'
edad = 51

nombre1 = 'Julia'
apellido2 = 'Roberts'
nombrecompleto = nombre1 +" "+ apellido2

curso = 'python'
print('Estás tomando un curso de', curso)


###################################################################################################################
edad = input('dime tu edad')
print('tu edad es' + edad)

edad_nueva = 1 + edad  #un dato que se ingrese en input siempre lo toma como un string y se tiene que pasar a entero
print('tu cumplirias' + edad_nueva)

print(type(edad_nueva))


num_entero = 10
print(type(num_entero))

num_decimal = 2.50
print(type(num_decimal))

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))