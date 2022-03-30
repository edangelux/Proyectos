//como podemos hacer referencia a los valores de un mismo objeto como puede ser un const, eso es lo que llega a realizar this, pero hay dos formas para acceder a un objeto

//primera forma
const reservacion = {
    nombre: 'eddy',
    apellido: 'torrez',
    total: 5000,
    pagado: false,
    informacion: function() {
        console.log(`El cliente ${reservacion.nombre} reservo y su cantidad a pagar es de ${reservacion.total}`);
    }
}

reservacion.informacion();

const reservacion2 = {
    nombre: 'elias',
    apellido: 'escobar',
    total: 5000,
    pagado: false,
    informacion: function() {
        console.log(`El cliente ${this.nombre} reservo y su cantidad a pagar es de ${this.total}`);
    }
}

reservacion2.informacion();

//this hace referencia al objeto al cual estas enviando a llamar 