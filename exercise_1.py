""" 
    Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
For
    A)  #LISTO# 	La cantidad de valores negativos ingresados.
    B)  #LISTO# 	La cantidad de valores positivos ingresados.
    C)  #LISTO# 	La cantidad de múltiplos de 15.
    D)  #LISTO# 	El valor acumulado de los números ingresados que son pares.
    E)  Desarrollar un programa que solicite la carga de 10 números e imprima la suma de lo últimos 5 valores ingresados.
    F)  #LISTO#     Desarrollar un programa que muestre la tabla de multiplicar de un número ingresado por teclado.

While
    G)  #LISTO#     Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado).
    H)  #LISTO#     Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 -16 -24, etc. 
"""




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
""" numeroInput_2=[]
suma_py=0
suma_valores_2=0

for i in range(10):
    numeroInput_py[i]= int(input("Ingrese un numero: ")) """




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