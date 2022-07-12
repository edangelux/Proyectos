#hay que hacer un programa que genere comisiones al usuario el 13%
#redondear y que haya 2 decimales



print('hola buenos dias, este programa ayudara a calcular tus comisiones')
nombre = input('Ingrese su nombre: ')
print(f'hola mucho gusto {nombre}, le pido que ingrese su numero de ventas')
ventas = float(input('Ingrese su numero de Ventas: '))
comisiones = ventas * 13 / 100
print('Su ganancia de comisiones es: $',round(comisiones,2))