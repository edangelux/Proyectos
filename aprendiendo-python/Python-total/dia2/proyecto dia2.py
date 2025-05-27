#hacer un codigo que calcule la comision que es de 13%
#preguntar nombre y cantidad de ventas, venta * 13/100

porcentaje = 13
nombre = input('cual es tu nombre?: ')
venta = int(input(('cuanto es la cantidad vendida: ')))
comision= round(venta * 13 / 100,2)
print(f'la comision de {nombre} es de {comision}')