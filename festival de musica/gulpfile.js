const {src, dest, watch } = require("gulp")
const sass = require("gulp-sass")(require("sass"))
const plumber = require('gulp-plumber')

function css(callback) 
{
    src('src/scss/**/*.scss')  //identifica sass
    .pipe(plumber())
    .pipe(sass())//compila
    .pipe(dest("build/css")) //se guarda en disco

    callback() //avisa a gulp cuando llegamos al final de funcion 
}

function dev(callback)
{
    watch("src/scss/app.scss", css)

    callback()
}


exports.css = css;
exports.dev = dev;