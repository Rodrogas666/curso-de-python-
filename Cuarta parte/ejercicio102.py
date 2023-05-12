from tkinter import *

ventana = Tk()
ventana.title("App Python")
ventana.geometry("350x350")

lblNombre = Label(ventana, text="...")
lblNombre.grid(column=0, row=0)

txtNombre = Entry(ventana, width=12)
txtNombre.grid(column=1, row=0)

def saludar():
    datoEntrada = txtNombre.get()
    lblNombre.configure(text=datoEntrada)
    
btnNombre = Button(ventana, text="Presiona el boton", command=saludar)
btnNombre.grid(column=2, row=0)
ventana.mainloop()    