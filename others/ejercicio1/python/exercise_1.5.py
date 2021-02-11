""" E) """
print("\nEjercicio E:")
suma=0
lista =[1,2,500,96,40,15,5,50,20,10]

for i in range(10):
    if (i>4):
        suma+= lista[i]
print("La suma de las ultimas 5 cifras es: ",suma)

""" E2) """
print("\nEjercicio E version 2:")
suma=0
for i in range(10):
    numero = int(input(str(i)+ ". Ingrese un numero para sumar los ultimos 5: "))
    if (i>4):
        suma+=numero
print("La suma de los ultimos 5 numeros es: ", suma)

""" E3) """
nElementos = int(input("Ingrese porfavor la dimension de la lista: "))
lista = list(range(0, nElementos))
suma=0

for i in range(nElementos):
    lista = int(input(str(i+1)+". Ingrese porfavor 10 numeros enteros: "))
    if (i>4):
        suma+=lista
print("La suma de los ultimos 5 numeros es: ",suma)