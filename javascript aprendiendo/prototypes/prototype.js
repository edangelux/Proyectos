/* objeto literal */
const producto = {
        nombre: 'tablet',
        precio: 500
}


//objeto constructor
function producto(nombre, precio) {
    this.nombre = nombre;
    this.precio = precio;
}

function formatear (producto) {
    return `el producto ${producto.nombre} tiene un precio ${producto.precio}`;
}


console.log(producto);

//como pueden ver digamos que es esta parte cambiamos los datos con funciones de formatear pero si lo hacemos en un proyecto seria realizar muchas funciones tras otras y se hace poco practico para eso existe prototype

//Prototype nos permitira crear funciones que solo se utilizan en un objeto en especifico
producto.prototype.formatear = function() {
    return `el producto ${this.nombre} tiene un precio ${this.precio}`;
}

