/* Ejercicio F */

document.write("Tabla de multiplicacion: <br>");
        var numeroInput = parseInt(prompt("Ingrese un numero para multiplicar: "));
        for(i=1; i<11; i++){
            tabla = (numeroInput * i);
            document.write("F) ",numeroInput,"x",i,"= ",tabla,"<br>");
        }
        document.write("<br>");