#Interfaz Grafica con Tkinter
#PASO 1. Importar las librerias
#import tkinter as tk
from tkinter import *
from tkinter import ttk


#PASO 2. Inicializar una ventana
pantalla=Tk()
pantalla.title("Python - Tkinter")
#pantalla.resizable(0,0)

#LABEL
titulo=ttk.Label(text="Tkinter Label",background="red")
titulo.grid(column=0,row=0)
titulo2=ttk.Label(text="Label - Tkinter",background="blue")
titulo2.grid(column=1,row=1)
titulo3=ttk.Label(text="Titulo3",background="green")
titulo3.grid(column=2,row=2)

#BOTONES
boton=ttk.Button(pantalla,text="Boton 1",width=10)
boton.grid(column=1,row=3)
boton2=ttk.Button(pantalla,text="Boton 2")
boton2.grid(column=1,row=4)
boton3=ttk.Button(pantalla,text="Boton 3")
boton3.grid(column=1,row=5)

#RadioBox - Checkbox
a=ttk.Combobox(pantalla,textvariable="Encender")
a.grid(column=0,row=6)
b=ttk.Radiobutton(pantalla,text="Seleccionar")
b.grid(column=0,row=7)
c=ttk.Radiobutton(pantalla,text="Seleccion2")
c.grid(column=0,row=8)

casilla=ttk.Checkbutton(pantalla,text="Opcion1")
casilla.grid(column=0,row=9)
casilla2=ttk.Checkbutton(pantalla,text="Opcion2")
casilla2.grid(column=0,row=10)
casilla3=ttk.Checkbutton(pantalla,text="Opcion3")
casilla3.grid(column=0,row=11)
casilla4=ttk.Checkbutton(pantalla,text="Opcion4")
casilla4.grid(column=0,row=12)
casilla5=ttk.Checkbutton(pantalla,text="Opcion5")
casilla5.grid(column=0,row=13)

#Entradas de datos por teclado - Entry

labelNombre=ttk.Label(pantalla,text="Ingrese su nombre: ")
labelNombre.grid(column=0,row=14)
nombre=ttk.Entry(pantalla)
nombre.grid(column=1,row=14)
labelCorreo=ttk.Label(pantalla,text="Ingrese su Correo:")
labelCorreo.grid(column=0,row=15)
correo=ttk.Entry(pantalla)
correo.grid(column=1,row=15)
labelCelular=ttk.Label(pantalla,text="Ingrese su Celular:")
labelCelular.grid(column=0,row=16)
celular=ttk.Entry(pantalla)
celular.grid(column=1,row=16)
botonEnviar=ttk.Button(pantalla,text="Registrarse")
botonEnviar.grid(column=1,row=17)
#SpinBox

spin=ttk.Spinbox(pantalla)
spin.grid(column=0,row=18)


#PASO 3. Activar la ventana
pantalla.mainloop()