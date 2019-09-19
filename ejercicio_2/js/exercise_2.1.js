function ejercicio_2_1(){
    var num1, num2, num3;

    num1=parseInt(prompt('Ingrese porfavor un numero: '));
    num2=parseInt(prompt('Ingrese porfavor un numero: '));
    num3=parseInt(prompt('Ingrese porfavor un numero: '));

        if (num1 < num2 && num1 < num3){
            document.write("El numero menor es: ",num1);
        }else if (num2 < num1 && num2 < num3){
            document.write("El numero menor es: ",num2);
        }else{
            document.write("El numero menor es: ",num3);
        }
}