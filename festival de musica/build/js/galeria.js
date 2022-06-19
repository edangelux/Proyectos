document.addEventListener('DOMContentLoaded', function(){
    iniciarapp();
});

function iniciarapp() {
    crearGaleria();
}

function crearGaleria() {
    const galeria = document.querySelector('.galeria-imagenes');

    for(let i = 1; i <= 12; i++ ) {
        const imagen = document.createElement('picture');
        imagen.innerHTML = `
            <source srcset="build/img/chiquito/${i}.webp" type="image/webp">
            <img loading="lazy" width="200" height="300" src="build/img/chiquito/${i}.jpg" alt="imagen galeria">
        `;
        imagen.onclick = function() {
            mostrarImagen(i);
        }

        galeria.appendChild(imagen);
    }
} 