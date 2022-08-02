menor = min(50, 96, 73, 19)
mayor = max(50, 96, 73, 19)

lista = [50, 96, 73, 19]

print(menor)
print(mayor)
print(f'el menor es {min(lista)} y el mayor es {max(lista)}')

nombre = 'Carlos'

print(min(nombre.lower()))


dic = {'c1': 45, 'c2': 11}

print(min(dic))
print(min(dic.values()))


lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)


lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)
print(rango)


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
print(max(diccionario_edades.values()))
print(edad_minima)
ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre)