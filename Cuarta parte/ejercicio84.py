#Crear una aplicación que solicite al usuario una cantidad de números para ingresar a una lista
#e imprimir la lista 

print("Cuántos números querés ingresar")
cantidadNumeros = input()

contadorNumeros = 1
listaNumeros = []

#Lectura de cantidad de números

while contadorNumeros <= int(cantidadNumeros):
    print("Ingresa un números en la posición " + str(contadorNumeros) + ":")
    numeroIngresado = input()
    listaNumeros.append(int(numeroIngresado))
    contadorNumeros +=1
    print(listaNumeros)
    