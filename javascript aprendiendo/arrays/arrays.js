//arreglo o arrays 

//const numeros = [] 
/* este es un syntaxis como indicativo que es un arreglo */

const numeros = [10, 20, 30, 40, 50]; //esta variable esta conteniendo estos valores dentro

console.table(numeros); /* .tablet es una tabla que sera una manera mejor de ver los datos en este caso */

/* tenemos que saber que los arrays van con posiciones por que es una cadena en esta la posicion 0 = 10 posicion 1 = 20, y asi nosotros identificamos la posicion del valor */

//acceder a los valores de un arreglo
console.log(numeros[4]); //veras que nos imprimira 50


//metodos de arrays

//agregar 

numeros.push(60); /* push es la manera de agregar un valor mas al arrays sin necesidad de saber de cuento es el limite del arrays el solo sabe que tiene que agregar eso al final */

numeros.unshift(-10); /* agregara al inicio del arreglo */

//eliminar

numeros.pop(); /* elimina el ultimo dato del arreglo */
numeros.shift();/* eliminara el primero del arreglo */

numeros.splice(2, 1); /* aca es desde la posicion dos cuanto quieres eliminar? tu puedes eliminar desde la posicion hacia adentalte yo solo elimine el de la posicion */

console.table(numeros);

// Rest Operator o Spread Operator

/* ya que es mejor no cambiar los datos originales del arrays lo mas eficiente seria copiarlo y ahi codificarlo */

const nuevo = [...numeros, '100']; /* aqui copiamos el arrays y luego de ello agregamos 100 */



/* array multidimencional */
/* array methods */


//esto es un  arreglo de objetos
const carrito = [
    {Nombre: 'monitor', precio: 500},
    {Nombre: 'television', precio: 700},
    {Nombre: 'tablet', precio: 300},
    {Nombre: 'audifonos', precio: 200},
    {Nombre: 'teclado', precio: 50},
    {Nombre: 'celular', precio: 500},
    {Nombre: 'bocinas', precio: 300},
    {Nombre: 'laptop', precio: 800},
];

//includes

/* se supone que el codigo de aqui es uno de los tantos metodos para encontrar un resultado de un arreglo
pero les dara mal por que esto es para un arreglo normal, nosotros tenemos un arreglo de objetos entonces no funcionara existe otro metodo */
const resultado = carrito.includes('celular');

//some ideal para arreglo de objetos
/* tienes que acceder a cada propiedad de lo que quieras comprobar para que todo funcione */
resultado = carrito.some(function(producto){
    return producto.nombre == 'celular'
})

//tambien se puede hacer el codigo asi
resultado = carrito.some(producto => producto.nombre === 'tablet')

//reduce es un metodo que calcula un valor final o anterior 
resultado = carrito.reduce(function(total, producto) {
    return total + producto.precio
}, 0);
/* lo que aqui hizo fue dar el valor total del carrito de compra de todos los productos */
//tambien se puede hacer asi
resultado = carrito.reduce((total, producto) => total + producto.precio, 0);

/* filter
 es para obtener filtros de datos especificos*/
resultado = carrito.filter(function(producto) {
    return producto.precio > 400
}); //lo que hizo es filtrar solo productos con valor mayor de 400


console.log(resultado);


