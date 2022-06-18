const {src, dest, watch} = require("gulp"); //extraer funcionalidades de gulp.file
const sass = require("gulp-sass")(require('sass')); //extraer funcionalidades sass descargando extension gulp-sass

//src = buscar dest = almacenar watch = observar cambios

function css (call){
    src('src/scss/**/*.scss') //identificar archivo de sass

    .pipe(sass()) // compilarlo

    .pipe(dest('build/css')); //guardarla

    call(); // avisa a gulp cuando llegamos al final
}

function dev (call){ //observar todo tipo de cambios de la hoja y se pasa a la funcion css
    watch('src/scss/**/*.scss', css)

    call();
}

exports.css = css;
exports.dev = dev;