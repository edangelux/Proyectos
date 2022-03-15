//es parte de las funciones llega  hacer parte importante para guardar todaa la informacion en un solo objeto, cuando podas crear un objeto grande, tienen a hacer una buena opcion de estructura veamos a continuacion


/* METODO DE PROPIEDAD */

//este reproductor tiene un objeto que tiene la funcion que se llama reproducir
const reproductor = {
    reproducir : function(id) {
        console.log(`reproduciendo cancion con el ID: ${id}`)
    },

    pausar : function(){
        console.log(`Pausando...`)
    },

    CrearPlaylist : function(nombre){
        console.log(`Creando playlist: ${nombre}`)
    },

    ReproducirPlaylist : function(nombre){
        console.log(`Reproduciendo Playlist: ${nombre}`)
    }
}

/* nota aqui esto en los objetos de reproducir y pausar tienen ":" dos puntos pero en este sera un signo igual por que en este caso estamos agregando propiedades por fuera del objeto*/
reproductor.borrar = function(id){
    console.log(`Eliminando la cancion: ${id}`);
}


/* console.log(reproductor); */

reproductor.reproducir(32); 
reproductor.pausar();
reproductor.borrar(20);
reproductor.CrearPlaylist('perreo pa la nenas');  
reproductor.ReproducirPlaylist('perreo pa la nenas');