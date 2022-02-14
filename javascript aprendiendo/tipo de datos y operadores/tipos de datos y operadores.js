'use strict'

 /* operadores */

 /* adicion  +
 sustraccion  -
 multiplicacion  *
 division  /
 resto  %
 
 operadores de comparacion
 
 igualdad ==
 desigualdad !=
 estrictamente iguales ===
 estrictamente desiguales !==
 mayor que >
 mayor o igual que >=
 menor que <
 menor o igual que <=
 
 operadores aritmetico
 
 incremento ++
 decremento --
 resto %
 
 operadores ternario
 
 condicion ? valor1 : valor2
 si la condicion es true tomara el valor1, sino el valor2*/
var numero1 = 5;
var numero2 = 10;
var operacion = numero1 + numero2;

alert(" el resultado de la operacion es: "+operacion); /* aca mostraria en un alert la respuesta total de la suma */
 
/* tipos de datos */
var number = 10; /* valor numerico puede ser entero o decimal */
var string = "a"; /* cadena de texto para ingresar texto que representan un valor*/
var boolean = true  //false /* es un valor logico que sus valores son verdadero o falso para hacer condiciones */
var //null /* denota valor nulo */
var undefined /* es decir un valor sin definir  */
var symbol /* cuyos datos son unicos o inmutables */
var object //{} /* puede contener mas variables en su interior */

    console.log(typeof number); /* typeof en la consola demostrara que tipo de dato esta hecha la variable */

    // booleano
    // valores de verdadero o falso    
const boolean1 = true;
const boolean2 = false;
 const boolean3 = "true"; /* aqui este lo tomara como un string puedes comprobar con un typeof  */

 console.log(boolean1);
 console.log(boolean2);

 // objetos 

  //un objeto puede contener mas variables en su interior mas o menos como un struct

/* manera normal  */
const nombreObjeto = "monitor"
const precio = 300
const disponible = true;

/* manera de objeto */
const producto = {
    nombre: "monitor",
    precio: 300,
    disponible: true
}

console.log(producto);

/* como puedo ingresar a el campo? */

console.log(producto.precio);

//modificar objeto

producto.imagen = 'imagen.jpg'; //agregar

delete producto.disponible; //eliminar 

console.log(producto);

//destructurar objeto

const producto1 = {
    nombre1: "teclado",
    precio1: 100,
    disponible1: true
}

//forma anterior
const precioProducto = producto1.precio1; //lo que hacemos es meternos a el objeto y extraemos el dato de precio1

console.log(precioProducto)


//nueva forma

const {precio1} = producto1; /* este codigo hace lo mismo que el otro pero de esta manera mas resumida */

console.log(precio1);

//objeto metodos

/* la situacion de un objeto si se puede modificar aunque tengas un const es parte limitante de un objeto o algo que puede afectar, como preveenir? */

object.freeze(producto1); /*  es una manera de decir de congelar el objeto y no se podra agregar mas propiedades */

console.log(object.isfrozen(producto1)); /* se supone que en esta syntaxis es una verificacion de saber si el objeto esta congelado */

object.seal(producto1) /* este no te permite agregar ni eliminar pero si modificar los objetos en freeze nada se puede hacer */