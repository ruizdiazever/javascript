function ejercicioTwo(){
    var numero1, numero2, numero3;

    numero1=parseInt(prompt('Ingrese porfavor un numero: '));
    numero2=parseInt(prompt('Ingrese porfavor un numero: '));
    numero3=parseInt(prompt('Ingrese porfavor un numero: '));

    menorMayor(numero1, numero2, numero3);

    function menorMayor(num1, num2, num3){
        if ( (num1<num2) && (num2 < num3) ){

            document.write(num,", ",num2,", ",num3)

        }else if ( (num2<num1) && (num1<num3) ){

            document.write(num2,", ",num1,", ",num3)

        }else{

            document.write(num3,", ",num2," ,",num1)
            
        }
    }
}