
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
//

class Libro extends Producto {
    constructor(nombre, precio, isbn){
        super(nombre, precio);
        this.isbn = isbn;
}

    formatearProducto() {
        return `${super.formatearProducto} y su isbn es ${this.isbn}`;
    }
}
//bueno veamos tenemos codigos simular repetido y aqui no estamos haciendo algo totalmente practico,entonces esto que aprenderemos se llamara HERENCIA y es igual que la vida real

//herencia es como una persona que en vida fallece se les da los vienes o los datos se los da alguien mas

//igualmente en el constructor se tienen que pasar herencias si ya pasaste herencia en la clase y tienes un constructor, esto se llama super() no podemos poner super() si alguna variable no esta en el constructor padre


const libro = new Libro('javascript te odio', 120, '1284983120a');

console.log(libro.formatearProducto());
console.log(Producto2.formatearProducto());