""" Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio """

def describir_persona(nombre,**kwargs):
 
    print(f"Características de {nombre}:")
 
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")
        
        
        """el programa va a elegir una palabra secreta y el jugador se le imprimira una serie de guiones que es la cantidad de letras que hay en 
        la palabra secreta el jugador por turno tiene que elegir una letra y si la letra se encuentra en la palabra secreta se mostrara en que posicion estaba esa letra 
        pero si el jugador no coloca una letra que hay en la palabra secreta entonces perdera una vida tienen 6 vidas en total y cada vez que pierda una se le dira
        y si adivina todo se le dira que gano y si pierde todas las vidas se le dira que perdio 
        usaremos choice 
        funciones
        """