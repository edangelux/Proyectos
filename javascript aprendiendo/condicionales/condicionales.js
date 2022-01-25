'use strict'

/* condicionales que aprenderemos */
/* condicionales es una estructura de control o unas instrucciones que nos van a permitir comparar algo
es decir si A es igual B entonces haz algo siguiente (mas o menos asi)*/

/* if = "si" edad1 es mayor a edad2
else = y si no es mayor pues ejecuta esto */
/* else if = si se cumple la primera condicion se ejecuta todo y si no pues validamos las distintas condiciones que estan en la linea de codigo */

var edad1 = 20;
var edad2 = 12;

/*si pasa esto*/
if(edad1 > edad2)
/* ejecuta esto */
{
    console.log("edad uno es mayor que edad2");

    if (edad1 >= edad2)
    {
        console.log("es mayor edad1");
    }
    else
    {
        console.log("entonces es mayor edad2");
    }
}
else {
    console.log("la edad uno es inferior");
}

/*  negacion*/

var year = 2018;
if (year != 2016)
{
    console.log("el año no es 2016");
}

/* and */
if(year >= 2000 && year <= 2020)
{
    console.log("estamos en era actual");
} else {
    console.log("estamos en era post moderna")
}

/* or */
if (year == 2008 || year == 2018)
{
    console.log("el año acaba en 8")
}
else {
    console.log("año no registrado");
}

/* switch = condicional que permite hacer multiples operaciones y tomar decisiones enn funcion de distintos estados de las variables, evalua una expresion comparando el valor de esa expresion con una instancia case, y ejecuta declaraciones asociadas a ese case asi como las declaraciones en los case que siguen */

var edad = 18;
var imprime = "";

switch(edad)
{
    case 18: /* sentencia a ejecutar si la expresion tiene el valor 18 */
        imprime = "acabas de cumplir la mayoria de edad";
    break;
    case 25: /* sentencia a ejecutar si la expresion tiene el valor 25 */
        imprime = "ya eres adulto";
    break;
    case 40: /* sentencia a ejecutar si la expresion tiene el valor 40 */
        imprime = "crisis de los cuarenta"
    break;

    default: /* sentencia a ejecutar si el valor no es ninguno de los anteriores */
        imprime ="no tienes edad";
    break;
}

console.log(imprime);