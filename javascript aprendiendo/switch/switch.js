 const metodopago = 'tarjeta';

 switch(metodopago) {
    case 'tarjeta':
         console.log('pagaste con tarjeta');
        break;
    
    case 'cheque':
        console.log('pagaste con cheque');
    break;

    case 'efectivo':
        console.log('pagaste con efectivo');
       break;
        
        
        
    default:
         console.log('aun no has pagado');
        break;
 }