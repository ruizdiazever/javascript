        var contador_negativo=0;
        var contador_positivo=0;
        var suma_pares=0;
        var tabla;
        var contador_multiplo=0;

        for (var i=1; i<=10; i++){
            numeroInput = parseInt(prompt(i+") Ingrese 10 numeros enteros por teclado: "));

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



    
        var numeroInput = new Array();
        var suma = 0;
        var suma_valores =0;

        for (i=1;i<=10;i++){
            numeroInput[i] = parseInt(prompt(i+") Ingrese 10 numeros enteros por teclado: "));
            if (i > 5){
            suma_valores = suma_valores+numeroInput[i];
            document.write("Posicion "+(i)+": "+numeroInput[i]+"<br>");
            }              
        }
        document.write("La suma de los ultimos 5 valores: ",suma_valores);  



     
        var numeroInput = parseInt(prompt("Ingrese un numero por teclado: "));
        for(i=1; i<11; i++){
            tabla = (numeroInput * i);
            document.write("F) ",numeroInput,"x",i,"= ",tabla,"<br>");
        }




    
        document.write("25 terminos de 11: <br>");
        var iterador = 1;
        var numero = 11;

        while (iterador <= 25 ){
            numero = 11 * iterador;
            document.write("Termino ",iterador,":   ",numero+"<br>");
            iterador++;
        }
    



    
        var multiplo = 8;
        var maximo = 500;
        document.write("<br>Multiplos de 8 hasta el 500: <br>");
        while (multiplo <= maximo){
            multiplo = multiplo * 2;

            document.write(multiplo+"<br>")
        }
    