from tkinter import *

def miFuncion():
    print("Este mensaje es del boton")

ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry("600x300")

lbl = Label(ventana, text="Este es un label")
lbl.config(bg="pink")
lbl.pack()

btn = Button(ventana, text="Presionar", command=miFuncion)
#btn.config(fg="black", bg="green")
btn["fg"]="red"
btn["bg"]="white"
btn.pack()

#para ejecutar directamente el archivo desde la carpeta del programa la aplicacion se ejecuta cambiando la extensión del archivo.py por .pyw
#al dar doble click se ejecuta el programa
ventana.mainloop()


