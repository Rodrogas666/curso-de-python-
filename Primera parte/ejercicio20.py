#Crear una aplicación para calcular el IMC

#IMC = peso / altura * altura

print("Por favor ingresa tu peso")
peso = input()

print("Por favor ingresa tu altura")
altura = input()

imc = float(peso) / (float((altura)) * float((altura))) #Sin los parentesis amarillos no funciona bien 
#Porque sino lo que hace es dividir y multiplicar, osea no multiplica con la otra altura

print("Tu índice de masa corporal es", imc)