from tkinter import *

ventana = Tk()
ventana.title("Hola Rodri")
ventana.geometry("350x350")


lblNombre = Label(ventana, text="Hola")
lblNombre.grid(column=0, row=0)

def saludar():
    lblNombre.configure(text="Hola pelotudo")
    
btnSaludar = Button(ventana, text="Saludar ahora", command=saludar)
btnSaludar.grid(column=1, row=0)
    

ventana.mainloop()