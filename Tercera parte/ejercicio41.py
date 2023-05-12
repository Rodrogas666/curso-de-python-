#Realiza una app que pida al usuario una cantidad determinada de números y muestre al usuario los números impares que existen en la longitud proporcionada

print("Ingresa la longitud de números a evaluar")
cantidad = int(input())
numero = 1

print("Estos son los siguientes números impares")

while numero < cantidad:
    if((numero % 2 != 0)):
        print(numero)
    numero += 1


    #SIEMPRE MIRÁ LA SANGRÍA

