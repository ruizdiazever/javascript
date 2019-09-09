print("Ejercicios A, B, C & D:")
""" A) B) C) D) """
numeroInput=0
contador_negativo=0
contador_positivo=0
suma_pares=0
tabla=0
contador_multiplo=0
for i in range(10):
    numeroInput=int(input("Introduce un numero: "))
    if numeroInput<0:
        contador_negativo+=1
    else:
        contador_positivo+=1
    if numeroInput%15==0:
        contador_multiplo+=1
    if numeroInput%2==0:
        suma_pares+=numeroInput

print("\nA) Numeros negativos: ",contador_negativo)
print("B) Numeros positivos: ",contador_positivo)
print("c) Multiplos de 15: ",contador_multiplo)
print("D) Suma de pares: ",suma_pares)



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




""" F) """
print("\nEjercicio F, tabla de multiplicar:")
tabla=0
numeroInput_3= int(input("Ingrese un numero: "))
for i in range (1,11,1):
    tabla = numeroInput_3*i
    print("F) ",numeroInput_3,"x",i,"= ",tabla,)




""" G) """
print("\nEjercicio G, 25 terminos de 11:")
contador_max = 0
numero = 0
aux = 11
while (contador_max < 25):
    numero= numero + aux
    contador_max+=1
    print(contador_max,"- Termino: ",numero)




""" H """
print("\nEjercicio H, multiplos de 8 hasta 500:")
multiplo=8
numero=8
maximo=500
while multiplo <= maximo:
    print(multiplo)
    multiplo = numero+multiplo