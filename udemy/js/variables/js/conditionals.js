'use strict'


var ever_edad = 27;    // 27 años
var sofia_edad = 0.91; // 11 meses

if(ever_edad > sofia_edad){
    console.log("Ever es " + (ever_edad - sofia_edad) + " años mas grande que su hija Sofia.")
}else{
    console.log("Edades incorrectas.")
}


var year = 18;
var namePerson = "Ascottino";

if (year >= 18){
    console.log(namePerson + " es mayor de edad.");
    
    if (year <= 33){
        console.log(namePerson + " es millenial.");
    }else if(year >= 70){
        console.log(namePerson + " no es millenial y es viejito.");
    }else{
        console.log(" ya no es millenial.")
    }
}else{
    console.log(namePerson + " es menor de edad.");
}


