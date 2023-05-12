#Ejercicio de condicional
#Comparar 2 edades e indicar cual es mayor, menor o igual respecto a los datos
#Edad de pedro y otra de pablo

print("Escribe la edad de Pedro")
edadPedro = int(input())

print("Escribe la edad de Pablo")
edadPablo = int(input())

if edadPedro > edadPablo:
    print("La edad de Pedro es mayor que la de Pablo")

elif edadPedro == edadPablo:
    print("La edad es igual")

else:
    print("La edad de Pablo es mayor")   
    #else no necesita condición 