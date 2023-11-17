#Componentes Avanzados Tkinter 09-11-2023
#1. Menus 
import tkinter as tk
from tkinter import ttk

def seleccion1():
    titulo.config(text="Opcion 1")

def seleccion2():
    titulo.config(text="Opcion 2")

def seleccion3():
    titulo.config(text="Opcion 3")

def seleccion4():
    titulo.config(text="Opcion 4")

def seleccion5():
    titulo.config(text="Opcion 5")

def seleccion6():
    titulo.config(text="Opcion 6", font=("Roboto",20))

def mostrarMenu(event):
    menuItems2.post(event.x_root, event.y_root)



ventana=tk.Tk()
ventana.title("Menus")





#Barra de menu inferior
menuInferior=tk.Frame(ventana,relief="raised", borderwidth=2,background="#7B898A")
menuInferior.pack(side="bottom",fill="x")

##Crear la barra del menu
menu_barra=tk.Menu(menuInferior)
ventana.config(menu=menu_barra)

menu_archivo=tk.Menu(menu_barra, tearoff=False)
menu_archivo.add_command(label="opcion1Infereior", command=seleccion1)
menu_archivo.add_command(label="opcion2Infereior", command=seleccion2)
menu_archivo.add_command(label="opcion3Infereior", command=seleccion3)
menu_barra.add_cascade(label="Menu Inferior", menu=menu_archivo)

boton1=tk.Button(menuInferior, text="Opcion1",command=seleccion1)
boton2=tk.Button(menuInferior, text="Opcion2",command=seleccion2)
boton3=tk.Button(menuInferior, text="Opcion3",command=seleccion3)
boton4=tk.Button(menuInferior, text="Opcion4",command=seleccion4)
boton5=tk.Button(menuInferior, text="Opcion5",command=seleccion5)
boton6=tk.Button(menuInferior, text="Opcion6",command=seleccion6)
boton1.pack(side="left")
boton2.pack(side="left")
boton3.pack(side="left")
boton4.pack(side="left")
boton5.pack(side="left")
boton6.pack(side="left")

barraProgreso=ttk.Progressbar(ventana, length=200, mode="determinate")
barraProgreso.pack()

titulo=tk.Label(ventana, text="")
titulo.pack()

ventana.mainloop()