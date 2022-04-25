/* un promises es una promesa refleja un valor que podra estar disponible, funciona como una promesa de vida real  */

const auntetificacion = new Promise( (resolve, reject) =>  { //hay dos funciones que existen con promise (resolve, reject) resolve = se ejecutara cuando la promesa cumpla, reject = si no se cumple la promesa
    const aut = true;

    if(aut) {

        resolve(''); //se cumplio

    } else {

        reject(); //no se cumplio

    }
})