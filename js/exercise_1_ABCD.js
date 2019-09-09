/* Ejercicios A, B, C & D */

var contador_negativo=0;
        var contador_positivo=0;
        var suma_pares=0;
        var tabla;
        var contador_multiplo=0;

        for (var i=1; i<=10; i++){
            numeroInput = parseInt(prompt(i+") Ingrese porfavor 10 numeros enteros: "));

            if (numeroInput < 0){
                contador_negativo++;
            }else if (numeroInput > 0){
                contador_positivo++;
            }

            if ((numeroInput%15) == 0){
                contador_multiplo++;
            }
            if (numeroInput%2 == 0){
                suma_pares+=numeroInput;
            }
        }
        document.write("A) Numeros negativos: ",contador_negativo,"<br>");
        document.write("B) Numeros positivos: ",contador_positivo,"<br>");
        document.write("C) Multiplos de 15: ",contador_multiplo,"<br>");
        document.write("D) Valor acumulado pares: ",suma_pares," de tipo ",typeof(suma_pares),"<br>");
        document.write("<br>");