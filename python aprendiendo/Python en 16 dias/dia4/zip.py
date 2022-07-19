#junta las duplas
#llega hasta el largo de la lista mas corta e

nombres = ['ana','hugo','valeria','juan']
edades = [65,29,42]
cuidades = ['lima', 'madrid','mexico']

combinar = list(zip(nombres, edades, cuidades)) #se tiene que castear en una lista

for nombre,edad,ciudad in combinar:
    print(f'{nombre} tiene {edad} a;os y vive en {ciudad}')



capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinar = list(zip(paises, capitales))
for paises,capitales in combinar:
    print(f'La capital de {paises} es {capitales}')


marcas = ['converse', 'adidas', 'shein'] 
productos = ['mochilas', 'zapatos', 'ropa']


mi_zip = zip(marcas, productos)


espa = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
port = ['um','dois', 'três', 'quatro', 'cinco']
ing = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espa,port,ing))