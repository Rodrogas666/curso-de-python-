a, b, c = 5, 4, 3

print(a)
print(b)
print(c)

print("Ingresá tres valores")
x, y, z = input(), input(), input()

suma = int(x) + int(y) + int(z) #Nota como en input el ingreso de datos es str por defecto, tenés que hacer el casting porque sino solo suma en una cifra, no una suma de digitos

print("La suma de los datos es", suma)
