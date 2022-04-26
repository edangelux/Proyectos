//async/await hace una manera de una funcion asincrona

function descargar_clientes () {
    return new Promise (resolve  => {
        console.log('descargando cliente, espere...');
        
        setTimeout( () => {
            resolve('los clientes estan descargados');
        }, 5000);


    })
}

async function app() {
    try {
        const resultado = await descargar_clientes ();
        console.log(resultado);
    }
    catch (error) {
        console.log(error);
    }
}


app();