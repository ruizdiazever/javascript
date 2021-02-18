'use strict'

// MULTIDIMENSIONAL ARRAY
var categorys = ["Action", "Terror", "Comedy", "Sci-Fi"];
var movies = ["Matrix", "Ghost in the Shell", "Stalker", "Interestellar"];

var cine = [categorys, movies];
console.log(cine);



// Access to element 'Sci-Fi' in array 'categorys'.
console.log(cine[0][3]);
// Access to element 'Ghost in the Shell' in array 'movies'.
console.log(cine[1][1]);



// Add element in array
movies.push("Batman");
console.log(movies);



// Exercise
var userMovie = "";

do{
    userMovie = prompt("Introduce tu pelicula: ");
    movies.push(userMovie);
}while(userMovie != "STOP");

console.log(movies);