function ejercicio_1_6(){
    var numero = parseInt(prompt("Ingrese un numero para multiplicar: "));
    for(i=1; i<11; i++){
        tabla = (numero * i);
        alert("F) "+numero+"x"+i+"= "+tabla);
    }
}