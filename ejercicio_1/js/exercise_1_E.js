function ejercicio_1_5(){
    var numeroInput = new Array();
    var suma = 0;
    var suma_valores =0;

    for (i=1;i<=10;i++){
        numeroInput[i] = parseInt(prompt(i+") Ingrese porfavor 10 para despues saber sus posiciones: "));
        if (i > 5){
        suma_valores = suma_valores+numeroInput[i];
        /* document.write("Posicion "+(i)+": "+numeroInput[i]+"<br>"); */
        }              
    }
    respuesta=("La suma de los ultimos 5 valores es: ",suma_valores+'\n');
    alert(respuesta);
}