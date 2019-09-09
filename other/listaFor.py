nElementos = int(input("Ingrese porfavor la dimension de la lista: "))
lista = list(range(0, nElementos))
suma=0

for i in range(nElementos):
    lista = int(input(str(i+1)+". Ingrese porfavor 10 numeros enteros: "))
    if (i>4):
        suma+=lista
print("La suma de los ultimos 5 numeros es: ",suma)