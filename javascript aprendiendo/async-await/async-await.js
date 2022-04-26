//async/await hace una manera de una funcion asincrona

function descargar_clientes () {
    return new Promise (resolve  => {
        console.log('descargando cliente, espere...');
        
        setTimeout( () => {
            resolve('los clientes estan descargados');
        }, 5000);


    })
}

function descargar_pedidos () {
    return new Promise (resolve => {
        console.log('descargando los pedidos...');

        setTimeout(() => {
            resolve('los pedidos fueron descargados');
        }, 3000);
    });
}
async function app() {
    try {/* 
        const clientes = await descargar_clientes ();
        const pedidos = await descargar_pedidos();
        console.log(clientes);
        console.log(pedidos); */


         // hacer doble consulta de async await
        const resultado = await Promise.all([descargar_clientes(), descargar_pedidos() ]);
        console.log(resultado[0]);
        console.log(resultado[1]);
        /* se coloca posicion cero y uno por que estamos en un arreglo y asi se imprime cada uno aparte */
    }
    catch (error) {
        console.log(error);
    }
}


app();