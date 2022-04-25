/* documet. es la funcion para tomar toda la validacion de un html en queryselector es para la funcion seleccionada con su identificador luego */

const boton = document.querySelector('#boton');

/* luego todo esto es lo que haremos con un evento entonces seria... boton sera llamada cuando inicie ese evento... entonces cuando el usuario de click se va a ejecutar una funcion */
boton.addEventListener('click', () => {
    Notification.requestPermission()
        .then(resultado => console.log(`el resultado es:${resultado}`));
});

if(Notification.permission == "granted")
{
    new Notification('esta es una notificacion', {
        icon: 'nano.png',
        body: 'gente de masaya'
    })
}