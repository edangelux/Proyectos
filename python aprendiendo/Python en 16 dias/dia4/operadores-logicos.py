# and = y
# or = o
# not = no

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool1 = (4 < 5) and (5 == 2+3)
print(mi_bool1)

mi_bool2 = 1 == 10 or 3 == 3
print(mi_bool2)

texto = 'esta frase'

mi_bool3 = ('frase' in texto) and ('breve' in texto)
print(mi_bool3)

mi_bool4 = not 'a' == 'a'
print(mi_bool4)


num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 < num3

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3

texto = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = 'éxito'
palabra2 = 'tecnología'
mi_bool = not (palabra1 in texto) and not (palabra2 in texto)