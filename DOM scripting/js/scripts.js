//tres maneras para seleccionar un objeto
//querySelector
//solo tomara un objeto
const heading = document.querySelector('.header__texto h2') //tomara entre 0 y 1
console.log(heading)

//querySelectorAll
//tomara todos los objetos con la etiqueta a
const enlaces = document.querySelectorAll('.navegacion a')
console.log(enlaces)

//getElementId
//funciona unicamente seleccionando ids
const id = document.getElementById('heading')
console.log(id)



// Crear html con createElement
// la mejor manera de como explicarlo es cuando colocas un articulo al carrito de compra se genera un html para que el usuario luego mire el articulo colocado automaticamente el codigo html

const html = document.createElement('A') //falta agregar los atributos, texto y clase 
// texto, clase, atributo
 html.href = 'nuevo__enlace.html'
 html.classList.add('navegacion__enlace')
 html.textContent = 'nuevo enlace'

 //agregarlo al documento seria asi
 const nav = document.querySelector('.navegacion')
 nav.appendChild(html)
 //osea tomamos esta clase y al tomarla diremos colocate este html

 console.log(html)

 //eventos de javascript

 //el add event listener es la funcion para poder iniciar un evento y cuando pase ese evento se va  ahacer todo lo que este dentro, en este caso diremos cuando se cargue toda la pagina haremos esto!
 window.addEventListener('load', function(){
     console.log(5)
 })

 // seleccionar elementos y asociarlas en un evento

 const enviar = document.querySelector('.boton--primario'); 
 enviar.addEventListener('click', function (evento)
 {
     console.log('enviando formulario');
     console.log(evento)

     //valida un formulario de todas las celdas completadas
     console.log(evento.preventDefault())
 })

 //eventos de los inputs y textarea

 const datos = {
     nombre: '',
     email: '',
     mensaje: ''
 }

 const nombre = document.querySelector('#nombre')
 const email = document.querySelector('#email')
 const mensaje = document.querySelector('#mensaje')


 nombre.addEventListener('input', leer)

 email.addEventListener('input', leer)

 mensaje.addEventListener('input', leer)

 function leer(e){
     //console.log(e.target.value)

     datos[e.target.id] = e.target.value
     console.log(datos)
 }

 //evento de submit

 const formulario = document.querySelector('.formulario')
 formulario.addEventListener('submit', function(evento){
      evento.preventDefault()

 //validar formulario
const {nombre, email, mensaje} = datos

if (nombre === '' || email === '' || mensaje === '')
{
    mostrarerror('todos los campos son obligatorios')

    return; //corta ejecucion de codigo
}

//crear alerta correctamente
mostrarmensaje('se envio correctamente')

 //enviar formulario
      console.log('Enviando formulario')
 })
// muestra que se envio
 function mostrarmensaje(mensaje) {
     const alerta = document.createElement('p');
     alerta.textContent = mensaje
     alerta.classList.add('correcto')

     formulario.appendChild(alerta)
     //desaparezca
     setTimeout(() => {
         alerta.remove()
     }, 3000);
 }
 //muestra error

 function mostrarerror(mensaje) {
     const error = document.createElement('p')
     error.textContent = mensaje
     error.classList.add('correcto')

     formulario.appendChild( alerta )

     //desaparecer 3s
     setTimeout(() => {
         error.remove()
     }, 3000);
 }