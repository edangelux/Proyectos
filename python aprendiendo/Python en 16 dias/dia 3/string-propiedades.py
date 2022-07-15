#son inmutables
#son multiplicables
#son multilineales
#verificar si contiene
#calcular longitud

n1 = 'Kari'
n2 = 'na'
print(n1 + n2)
print(n1 * 10) #se repite hasta 10 veces

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema) #las comillas triple lo que hace es hacer saltos de linea dentro de ellas
print('agua' in poema) #le prguntamos si existe la palabra en el poema y te constestara en booleano
print('sol' not in poema) #le preguntamos si no esta en poema



print('Repetición' * 15)

p = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print('agua' not in p)

a = 'electroencefalografista'
print(len(a))