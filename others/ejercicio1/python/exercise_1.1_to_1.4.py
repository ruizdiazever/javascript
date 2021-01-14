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