""" Práctica Comprensión de Listas 1
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5] """

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_cuadrado = [i**2 for i in valores]
print(valores_cuadrado)  # [1, 4, 9, 16
