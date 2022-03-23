//es una forma de agregar funciones es nueva, su sintaxis es mas corta como tal 

//arrow functions
 const sumar = function(n1, n2) {
     console.log( n1 + n2);
 }
 sumar(5, 10); 

 //arrow funcion funciona cuando tenemos algo como este codigo como tal y tambien funciona bien con arrays methods pero cambia syntaxis asi:

 const sumar1 = (n3, n4) => {
     console.log(n3 + n4);
 }
 sumar1( 10, 10)

 // const nombre = () => {}

 const aprendiendo = (lenguaje) => {
     console.log(`Aprendiendo ${lenguaje}`)
 }
 aprendiendo('Javascript')

 //para codigo mas limpio y si no es extenso podremos hacer esto si el parametro y acciones son unicas como esto:

 const aprendiendo1 = lenguaje1 => console.log(`aprendiendo ${lenguaje1}`)
 aprendiendo1('c')

 //array metodos en arrow functions

 //arreglo o arrays 


const numeros = [10, 20, 30, 40, 50]; 

console.table(numeros); 
console.log(numeros[4]); 

numeros.push(60); 

numeros.unshift(-10); 

numeros.pop();
numeros.shift();

numeros.splice(2, 1); 
console.table(numeros);


const nuevo = [...numeros, '100']; 



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


const resultado = carrito.includes('celular');


resultado = carrito.some(producto => producto.nombre == 'celular');


resultado = carrito.some(producto => producto.nombre === 'tablet')


resultado = carrito.reduce((total, producto) => total + producto.precio, 0);


resultado = carrito.reduce((total, producto) => total + producto.precio, 0);


resultado = carrito.filter(producto => producto.precio > 400);

resultado = carrito.filter(producto => producto.nombre !== 'celular');

console.log(resultado);


