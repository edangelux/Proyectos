

lista = [letra for letra in 'python']


print(lista)

lista1 = [n for n in range(0,21,2)]
print(lista1)


lista2 = [n for n in range(0,21,2) if n * 2 > 10]
print(lista2)


lista3 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]



pies = [10,20,30,40,50]
metros = [p / 3.2808 for p in pies]




valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [n * n for n in valores]



valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n % 2 == 0]
print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(g-32)*(5/9) for g in temperatura_fahrenheit]
print(grados_celsius)