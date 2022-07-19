#tomar un fragmento de que buscaste y colocarlo en una variable
#se le llama slicing(rebanar)

texto = 'ABCDEFGHIJKMLNOQ'
rebanar = texto[2:5] #toma desde el 2 hasta el 4 osea no tomaria el 5 pero llega hasta el 5
print(rebanar)


texto1 = 'ABCDEFGHIJKMLNOQ'
rebanar1 =  texto1[:5] #toma todos hasta el tope
print(rebanar1)

texto3 = 'ABCDEFGHIJKMLNOQ'
rebanar3 = texto3[2:] #toma desde el dos hasta el tope
print(rebanar3)

texto2 = 'ABCDEFGHIJKMLNOQ'
rebanar2 = texto[2:10:2]
print(rebanar2)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
invertir = frase[::-1] #invertir texto
print(invertir)

frase = "Controlar la complejidad es la esencia de la programación"
cortar = frase[0:9]
print(cortar)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
cortar = frase[8::3]
print(cortar)