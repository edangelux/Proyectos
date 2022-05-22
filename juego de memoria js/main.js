//iniciar variables
let tarjetasVolteadas = 0;


// vamos a desordenar primeramente los botones
let numeros = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8];
//usamos la funcion sort y math.random para poder realizar el desorden
numeros = numeros.sort(() => {return Math.random() -0.5});

//funcion principal
function destapar(id){
    //cada vez que se voltee una tarjeta se sumara la cantidad
    tarjetasVolteadas++;

    if(tarjetasVolteadas == 1)
    {
        //mostrar contenido
        
    }

}

