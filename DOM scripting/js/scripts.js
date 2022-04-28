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