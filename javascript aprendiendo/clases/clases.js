// las clases revoluciono la programacion orientada a objetos
// class y seguido con el nombre de la clase podemos ver la syntaxis
// LAS CLASES SIEMPRE INICIALAS EN MAYUSCULAS POR BUENAS PRACTICAS


//la manera de como pasar los valores a la clase es un poco diferente ya que pueden ver que notiene los parentesis para tomar los parametros

//se utilizara constructor, que es contructor es una funcion sin tener la palabra funcion
class Producto {
    constructor(nombre, precio) {
         this.nombre = nombre;
         this.precio = precio;
    }

    formatearProducto() {
        return `El producto ${this.nombre} tiene un precio de: $ ${this.precio}` 
    }
}

const Producto2 = new Producto('monitor curvo de 49', 800 );
const Producto3 = new Producto('laptop', 300);

console.log(Producto2);
console.log(Producto3);