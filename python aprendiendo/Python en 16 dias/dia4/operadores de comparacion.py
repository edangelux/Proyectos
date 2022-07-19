#valores de comparacion
"""cuando asiganmos un valor a algo se usa el signo '='
cuando queremos comparar el valor de algo se usa el signo'==' """

mi_bool = 10 == 25
print(mi_bool)

mi_bool1 = 'blanco' == 'negro'
print(mi_bool1)

mi_bool2 = 'blanco' == 'blanco'
print(mi_bool2)

mi_bool3 = 'blanco' == 'Blanco'.lower()
print(mi_bool3)


num1 = 36
num2 = 17
mi_bool = num1 >= num2

num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2

num1= 64 * 3
num2= 24 * 8
mi_bool= num1 != num2