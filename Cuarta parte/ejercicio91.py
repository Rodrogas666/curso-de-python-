#Hacer una app que calcule el imc y mostrarle si tiene peso: bajo, normal o es un puto gordo
#peso / estatura * estatura
#IMC > 18.5 es peso bajo, IMC 18.5 >= y < 29.9 normal, IMC >= 29.9 gordo puto

def calculoIMC(estatura, peso):
    IMC = peso / (estatura * estatura)

    if IMC < 18.5:
        print("Peso bajo")
    else:
        if IMC > 18.5 and IMC < 29.9:
            print("Peso normal")    
        else:
            if IMC > 29.9:
                print("Gordo puto")  
            
            
                    
print("Poné tu estatura (m)")
estatura = float(input())

print("Poné tu peso (k)")
peso = float(input())


calculoIMC(estatura, peso)