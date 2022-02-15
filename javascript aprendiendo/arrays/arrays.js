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