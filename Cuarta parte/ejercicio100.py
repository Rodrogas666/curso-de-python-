from tkinter import *

ventana = Tk()
ventana.title("Hola Rodri")
ventana.geometry("250x250")#Ancho y alto

btnSaludar = Button(ventana, text="Saludar ahora")
btnSaludar.grid(column=0, row=0)
ventana.mainloop()
