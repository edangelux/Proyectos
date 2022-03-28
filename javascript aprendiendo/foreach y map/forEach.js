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

//for Each
//solamente se puede ejecutar en arreglos, es decir son metodos exclusivos de arreglos se va ejecutando por cada elemento que haya en un arreglo, esto existe en js

carrito.forEach( producto => console.log(producto.Nombre));

// MAP
 carrito.map(producto => console.log(producto.precio)); 

 //diferencias o casos de usar foreach y map
// cuando quieras iterar sobre un listado o mostrar elementos y enviarlos solo a la consola usa foreach
//si quieres crear un nuevo arregloo entonces usa el map

//ejemplo

const arreglo1 = carrito.forEach(producto => (producto.Nombre));

const arreglo2 = carrito.map(producto => (producto.Nombre));

console.log(arreglo1)
console.log(arreglo2) 
// solo un console.log dara el dato mas amplio que sera map y es por eso que se usa parqa un arreglo o dato nuevo
