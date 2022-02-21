//FUNCIONES

/* una ventaja de las funciones es que te permiten tener un codigo mas ordernado y mas faciol de mantener 
son reutilizables puedes tener una funciones que valuide un formulario y utilizarla en todos tus formularios. Existe 3 formas de crear funciones*/

//declaracion de funciones


function sumar() { //aqui cree la funcion
    console.log(10 + 10);
}

sumar(); //aqui mande a llamar la funciones

//expresion de la funcion
const sumar2 = function() {
    console.log( 2 + 2 );
}

sumar2();

//IIFE
/* basicamente son funciones que no necesitan llamarse por que se mandan llamar ellas mismas */
(function() {
    console.log('esto es una funcion');
})();

//diferencias entre metodos y funciones
const numero1 = 20;
const numero2 = "20";

console.log( parseInt(numero2)); //esto es una funciones
console.log( numero1.toString()); //esto es un metodo
/* como se diferencian? pues como tal una metodo es el que esta despues de la variable y se agrega un punto ejemplo: variable.toString, mientras que una funciones va antes de la variable por ejemplo:
parseInt(numero2) */



// FUNCIONES CON PARAMETROS Y ARGUMENTOS

function sumar3(n1= 0, n2 = 0) { //aqui le estamos pasando parametros que es n1 y n2 variables colocadas
    console.log(n1 + n2);
}
sumar3(10, 10) //argumentos o valores reales
sumar3(1); //si en dado caso no hay otro valor en n2 pues tomaria el default que es 0 

// FUNCIONES QUE RETORNEN VALORES
/* el punto de eston son variables que retornen resultado osea que si sumo que me retorne el resulta ya para meterlo dentro de una variable con ese valor */

function sumar4(n1, n2) {
    return n1 + n2;
}

const resultado = sumar4(2, 2);

//un ejemplo mas avanzado a carrito

let total = 0;

function Carrito2(precio) {
    return total += precio;
}

function Impuesto(total) {
    return 1.15 * total;
}

total = Carrito2(100);
total = Carrito2(200);

console.log(total);

const totalpagar = Impuesto(total);
console.log('el total a pagar es de: $${totalpagar}');