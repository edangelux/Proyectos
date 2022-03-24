 const puntaje = 1001;

 if (puntaje == 1000) {
    console.log('si el puntaje es 1000');
 }
 else {
     console.log('no es igual');    
 }

 //javascript tiene un comparador de 3 signos de igualacionn: "===" funciona como el de dos "==" pero se supone que es un poco mas estricto

 const efectivo = 1000;
 const carrito = 800;

 if (carrito < efectivo) {
    console.log(' el usuario puede pagar');
 }
 else {
     console.log('fondo insuficiente');
 }

 //else iff

 const rol = 'Administrador';

 if (rol === 'Administrador') {
     console.log('Acceso a todo el sistema');
 }
 else if (rol === 'Editor') {
    console.log('eres editor, hola editor')
 }
else {
    console.log('no tiene acceso');
}