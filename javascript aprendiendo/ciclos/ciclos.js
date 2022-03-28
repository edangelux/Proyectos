//algunas veces deseas ejecutar un codigo que queres que se repita la accion hasta  que se cumpla o se deje de cumplir, bueno entonces eso se hace con for

//FOR LOOP
// un for loop va ejecutando un codigo mientras una condicion sea evaluada como verdadero y se deja ejecutar

for(let i = 1; i <= 100; i++)
{
    if( i % 2 === 0)
    {
        console.log(`El numero ${i} es par`);
    }
    else 
    {
        console.log(`El numero ${i} es impar`);

    }
}

const carrito = [
    {Nombre: 'monitor', precio: 500},
    {Nombre: 'television', precio: 700},
    {Nombre: 'tablet', precio: 300},
    {Nombre: 'audifonos', precio: 200},
    {Nombre: 'teclado', precio: 50},
    {Nombre: 'celular', precio: 500},
    {Nombre: 'bocinas', precio: 300},
    {Nombre: 'laptop', precio: 800},
];

for(let x = 0; x < carrito.length; x++)
{
    console.log(carrito[x].Nombre);
}

//while 
//es igual que que for pero mantiene sus diferencias, un while se ejecuta mientras la condicion sea evaluada como verdadera

let y = 0 //primero vas la variable

while(y <= 100) { //la condicion

    if( y % 2 === 0)
        console.log(`el numero ${y} es par`)
    y++// lo aumentado ira de ultimo
}

//do while
// do while ejecuta el codigo al menos una vez y luego evalua a diferencia del while
let i = 0

do {

    i++
} while( i < 10)

//diferencia de while y do while

//while revisara las condiciones y si no es verdadero no se ejecuta 
//do while se ejecutara una vez el codigo y despues de eso validara o no las condiciones