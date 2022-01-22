 /* diferencia de "let" y var es que es limitada su alcance al bloque declarado que se esta usando de acuerdo y "var" define una variable global o local en una funcion sin importar el ambito del bloque */


 // var y let probemos
 /* como tal se supone que aca alteraria el valor de var numero 2 veces dandole valores primero de 40 y luego de 50 */
 var numero = 40;
console.log(numero); //aca el resltado en consola seria 40

if (true) {
    var numero = 50; 
    console.log(numero); //seria el valor 50
}

console.log(numero); //aca tambien 50

/* prueba con let */
var texto = "prueba";
console.log(texto); //daria el valor el mismo 

if (true)
{
    let texto = "prueba con let ";
    console.log(texto) /* saldria en consola el texto "prueba con let" */
}

/* let actua a nivel de bloque osea como tal solo estaria actuando dentro del if unicamente*/

console.log(texto) //<- aca saldria el texto "prueba" por que var es de manera global y let de manera de bloque 