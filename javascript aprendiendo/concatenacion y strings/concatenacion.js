/* concatenacion */

const nombre ='Eddy';
const email = 'eddytorrez34@gmail.com';

console.log(nombre +" "+ email); /* este codigo dice: mas agregamos espacio mas el email */
console.log(nombre, " ", email); /* lo mismo que "+" pero esta vez con "," */

//template string - string literals

console.log(`${nombre} ${email}`);  

/* importante poner estas comillas raras ``, luego de eso ponemos: ${variable} esto es para que el interprete lo entienda que es una variable y no string asi lo trate unicamente como variable */
