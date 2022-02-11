/* los string o cadenas de texto representan un texto que se puede asignar a la variable */
/* las comillas dobles o sencillas no se pueden mezclar asi: 'hola", "hola' */


/* primer metodo y esta es la mas conocida o usada*/
const hola = '"como estas"';
/* segundo metodo */
const hola1 = String('"como estas"');
/* tercer metodo pero al final termina siendo un objeto */
const hola2 = new String('"como estas"');

console.log( typeof hola)
console.log( typeof hola1)
console.log( typeof hola2)

console.log( typeof hola.length) /* <- ahi te dice el numero de los caracteres */
console.log(hola.indexOf('como')); /* esta funcion indexOf hace una busqueda de palabra y retorna posicion */
console.log(hola.includes('como')); /* esta funcion es lo mismo que indexOf pero retorna true o false */
