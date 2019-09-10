lista = []
suma=0
for i in range (10):
    lista[i] = int(input("Introduzca un numero: "))
    if (i<10):
        suma+= lista[i]
print("La suma de las ultimas 5 cifras es: ",suma)




print("**********************************************")
suma=0
lista =[1,2,500,96,40,15,5,50,20,10]

for i in range(10):
    if (i>4):
        suma+= lista[i]
print("La suma de las ultimas 5 cifras es: ",suma)




print("**********************************************")
contador=0
for i in range(3,12,2):
    print("El numero ",i, " es impar.")
    contador+=1
print(u"El ultimo for iteró",contador, "veces.")




print("**********************************************")
contador=0
for i in range(2,20,2):
    print("El numero ",i," es par.")




print("**********************************************")
nElementos = int(input("Ingrese porfavor la dimension de la lista: "))
lista = list(range(0, nElementos))
suma=0

for i in range(nElementos):
    lista = int(input(str(i+1)+". Ingrese porfavor 10 numeros enteros: "))
    if (i>4):
        suma+=lista
print("La suma de los ultimos 5 numeros es: ",suma)
