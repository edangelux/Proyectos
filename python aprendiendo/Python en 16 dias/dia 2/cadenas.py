#funcion format
color = 'black'
matricula = 12343212

print('mi auto es {} y su matricula es {}'.format(color, matricula))

#cadenas literales
print(f'mi auto es {color} y su matricula es{matricula}')

x = 10
y = 5
print('los numeros son {} y {} y la suma es{}'.format(x,y,x+y))


nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f'Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}')

puntos_nuevos = 350
puntos_totales = 1225
print('Has ganado {} puntos! En total, acumulas {} puntos'.format(puntos_nuevos,puntos_totales))

puntos_anteriores = 875
puntos_nuevos = 350
print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos')