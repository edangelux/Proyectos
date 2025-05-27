""" Práctica Comprensión de Listas 2
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5] """

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)  # [2, 4, 6]