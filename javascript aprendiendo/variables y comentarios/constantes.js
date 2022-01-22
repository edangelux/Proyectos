/* constante es un contenedor de datos al igual que una variable simplemente que ese valor no va  a poder ser modificado en nuestro programa */

var web = "https://eddy.com";
const ip = "192.08.0.12";

web = "https://elias.com";
ip = "00.00.0.00"; /* esta definicion no sera posible por que ya esta definida y no se podra cambiar nuevamente */

console.log(web, ip);