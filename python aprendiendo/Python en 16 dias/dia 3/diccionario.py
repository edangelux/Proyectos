# un diccionario funciona con palabras y al lado existe su definicion
# las palabras o claves no pueden repetirse
# no tiene un orden especifico

"""paciente = {
    'nombre':'Manuel',
    'apellido':'Pretti',
    'peso':82.6,
    'talla':1.78
}"""

diccionario = {'dato1':'valor1', 'dato2':'valor2'}
print(diccionario)


paciente = {
    'nombre':'Manuel',
    'apellido':'Pretti',
    'peso':82.6,
    'talla':1.78
}

consulta = paciente['apellido']

dic = {'a1':55,'a2':[10,20,30],'a3':{'s1':100,'s2':200}}
print(dic['a3'])
print(dic['a3']['s2'])

dic1 = {'a1':['a','b','c'], 'a2':['d','e','f']}
print(dic1['a2'][1].upper()) #para usar el upper en diccionario tienes que seleccionar el index

dic2 = {1:'a',2:'b'}
dic2[3] = 'c'
print(dic2)
dic2[2] = 't'
print(dic2)

print(diccionario.keys()) #imprimir las llaves
print(diccionario.values())#imprime los valores de las llaves
print(diccionario.items())#imprime todo lo que haya en el diccionario


#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['pais'] = 'Colombia'
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'