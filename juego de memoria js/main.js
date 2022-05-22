//iniciar variables
let tarjetasVolteadas = 0;
let tarjeta1 = null;
let tarjeta2 =  null;
let resultado1 = null;
let resultado2 = null;
let movimientos = 0;
let aciertos = 0;
let temporizador = false;
let time = 30;
let tiempo_inicial = 30
let detener = null

let winAudio = new Audio('./sounds/ganaste.wav');
let bienAudio = new Audio('./sounds/buena.wav');
let malaAudio = new Audio('./sounds/error.wav');
let perdisteAudio = new Audio('./sounds/perdiste.wav');
let clickAudio = new Audio('./sounds/click.wav');


//accediento al html
let mostrarleMovimientos = document.getElementById('movimiento');
let mostrarleAciertos = document.getElementById('aciertos');
let mostrarleTiempo = document.getElementById('tiempo-restante');


// vamos a desordenar primeramente los botones
let numeros = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8];
//usamos la funcion sort y math.random para poder realizar el desorden
numeros = numeros.sort(() => {return Math.random() -0.5});
console.log(numeros)

//funciones
// haremos el temporizador se resta cada 1s
function tiempo(){
    detener = setInterval(()=> {
        time--;
        mostrarleTiempo.innerHTML = `Tiempo: ${time} segundos`

        //cuando llegue a cero se detiene todo
        if(time == 0)
        {
            clearInterval(detener);
            bloquearTodo();
            perdisteAudio.play();
        }
    },1000)
} 

//hacemos la funcion para que se bloquee las tarjetas
function bloquearTodo()
{
    //15 = numero de tarjetas
    for(let i = 0; i<= 15; i++)
    {
        let tarjetaDetener = document.getElementById(i);
        tarjetaDetener.innerHTML = `<img src="./img/${numeros[i]}.png" alt="aqui se mostraria imagen">`;
        tarjetaDetener.disabled = true;
    }
}

//funcion principal
function mostrar(id){

    //cuando inicie todo comenzara el contador a restarse
    if(temporizador == false)
    {
        tiempo();
        temporizador = true;
    }

    //cada vez que se voltee una tarjeta se sumara la cantidad
    tarjetasVolteadas++;

    if(tarjetasVolteadas == 1)
    {
        //mostrar contenido
        tarjeta1 = document.getElementById(id);
        //darle el contendio al usuario
        resultado1 =  numeros[id];
        tarjeta1.innerHTML = `<img src="./img/${resultado1}.png" alt="aqui se mostraria imagen">`;
        clickAudio.play();

        //desahabilitar primera tarjeta para que no aumente el contador
        tarjeta1.disabled = true;
    }
    //validacion de tarjeta2
    else if(tarjetasVolteadas == 2)
    {
        //mostrar segundo contenido
        tarjeta2 = document.getElementById(id);
        resultado2 = numeros[id];

        //mostrarle al usuario el contenido
        tarjeta2.innerHTML = `<img src="./img/${resultado2}.png" alt="aqui se mostraria imagen">`;
        clickAudio.play();

        //desahabilitar segunda tajeta para que no aumente el contador
        tarjeta2.disabled = true;

        //incrementar el numero de movimientos
        movimientos++;
        mostrarleMovimientos.innerHTML = `Movimientos: ${movimientos}`;

        //validar si las tarjetas destapadas son las mismas
        if(resultado1 == resultado2)
        {   
            //si fue acertada que pueda volver a voltear mas tarjetas
            tarjetasVolteadas = 0;

            //aumentar aciertos
            aciertos ++;
            mostrarleAciertos.innerHTML =  `Aciertos: ${aciertos}`;
            bienAudio.play();

            if(aciertos == 8)
            {   winAudio.play();
                clearInterval(detener);
                mostrarleAciertos.innerHTML = `Aciertos: ${aciertos} 🎉🎊 `
                mostrarleMovimientos.innerHTML = `Movimientos:  ${movimientos}🤌🏼🥷`
                //resta el tiempo inicial con el que quedo guardo: 30 - 10 = 20segundos
                mostrarleTiempo.innerHTML = `Fantastico 🎉🎊 solo te demoraste: ${tiempo_inicial - time} segundos`
            }

        }
        else 
        {
            malaAudio.play();
            //en caso que no sean iguales vamos a mostrar los contenidos y volver a tapar
            setTimeout(()=>{
                tarjeta1.innerHTML = ' ';
                tarjeta2.innerHTML = ' ';
                tarjeta1.disabled = false;
                tarjeta2.disabled = false;
                tarjetasVolteadas = 0;
            },1000);

        }
    }
}

