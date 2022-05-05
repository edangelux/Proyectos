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