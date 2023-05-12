#App IMC
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("App calculadora de IMC")
ventana.geometry("250x250")

lblPeso = Label(ventana, text="Peso:")
lblPeso.pack()

txtPeso = Entry(ventana, width=12)
txtPeso.pack()

lblAltura = Label(ventana, text="Altura: ")
lblAltura.pack()

txtAltura = Entry(ventana, width=12)
txtAltura.pack()

def calculo():
    peso = int(txtPeso.get())
    altura = float(txtAltura.get())
    imc = peso / (altura * altura)
    
    messagebox.showinfo("App calculadora de IMC", "Tu IMC es: " + str(imc))
    if imc < 18.5:
        messagebox.showwarning("Peso...", "Peso bajo")
    else:
        if imc > 18.5 and imc < 29.9:
            messagebox.showinfo("Peso...", "Peso normal")
        else:    
            if imc > 29.9:
                messagebox.showerror("Peso...", "Peso alto")
    
btnCalcular = Button(ventana, text="Calcular IMC", command=calculo)
btnCalcular.pack()

ventana.mainloop()