const {src, dest, watch, parallel} = require("gulp"); //extraer funcionalidades de gulp.file

//css
const sass = require("gulp-sass")(require('sass')); //extraer funcionalidades sass descargando extension gulp-sass
const plumber = require('gulp-plumber');
//src = buscar dest = almacenar watch = observar cambios

//imagenes
const cache = require('gulp-cache');
const imagemin = require('gulp-imagemin');
const webp = require('gulp-webp')
const avif = require('gulp-avif')

function css (call){
    src('src/scss/**/*.scss') //identificar archivo de sass
        .pipe(plumber())// si hay errores no detiene el workflow

        .pipe(sass()) // compilarlo

        .pipe(dest('build/css')); //guardarla

    call(); // avisa a gulp cuando llegamos al final
}

function webpp(call){
    
    const opciones = {
        quality: 50
    };

    src('src/img/**/*.{png,jpg}')
    .pipe(webp(opciones))
    .pipe(dest('build/img'))

call()
}
    
function aviff(call){
    
    const opciones = {
        quality: 50
    };

    src('src/img/**/*.{png,jpg}')
    .pipe(aviff(opciones))
    .pipe(dest('build/img'))

call()
}

function imagenes(call){
    const opciones = {
        optimizationLevel: 3
    }

    src('src/img/**/*.{png,jpg}')
        .pipe(cache(imagemin(opciones)))
        .pipe(dest ('build/img'))
    
    call();
}

function dev (call){ //observar todo tipo de cambios de la hoja y se pasa a la funcion css
    watch('src/scss/**/*.scss', css)

    call();
}

exports.css = css;
exports.imagenes = imagenes;
exports.webpp = webpp;
exports.aviff = aviff
exports.dev = parallel(webpp, imagenes, dev);