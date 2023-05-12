from tkinter import *
from tkinter import messagebox #Un pop up es una ventana emergente que aparece de forma repentina encima del contenido que estás viendo en la primera ventana del navegador.

ventana = Tk()
ventana.title("Creador de mensajes")
ventana.geometry("350x350")

def mostrarMensajes():
    messagebox.showinfo("Mensaje", "De la app de mensajes")
    messagebox.showwarning("Sexo", "Sí")
    messagebox.showerror("Error", "No te ama")
    
    respuesta1 = messagebox.askquestion("Título", "Sos gay")
    respuesta2 = messagebox.askyesno("Hola", "Gay")
    
    messagebox.showinfo("Mira tu respuesta", "La cual fue " + str(respuesta1))
    
btnMostrador = Button(ventana, text="Mostrar mensaje", command=mostrarMensajes)
btnMostrador.grid(column=0, row=0)
ventana.mainloop()    