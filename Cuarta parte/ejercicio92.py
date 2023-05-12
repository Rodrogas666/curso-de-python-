#Clase
class calcularIMC:
    #El self hace referencia al nombre del objeto en el que se encuentra escrito. Lo podrías reemplazar por el nombre de la clase
    def __init__(self, peso, estatura):
        self.peso = peso
        self.estatura = estatura
        
    def imprimirIMC(self):
        self.imc = self.peso / (self.estatura * self.estatura)
        print("El IMC es: " + str(self.imc))
        
class mostrarPesoIdeal(calcularIMC):
    #Herencia, porque proviene de la clase padre
    def imprimirPeso(self):
        if self.imc < 18.5:
            print("Peso bajo")
        else:
            if self.imc < 18.6 and self.imc < 29.9:
                print("Peso normal") 
            else:
                if self.imc > 29.9:
                    print("Puto gordo")   
            
    
#Instancia, creación de un objeto a partir de una clase    
objCalcularIMC = calcularIMC(80, 1.7)    
objCalcularIMC.imprimirIMC() 

obj2CalcularIMC = calcularIMC(50, 1.7)
obj2CalcularIMC.imprimirIMC()

obj3CalcularIMC = mostrarPesoIdeal(30, 1.7)
obj3CalcularIMC.imprimirIMC()
obj3CalcularIMC.imprimirPeso()