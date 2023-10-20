#Crear una calculadora simple con estilos
import tkinter as tk
from tkinter import ttk

#Paso 2- Funciones de la calculadora
#funcion para calcular las operaciones
#Funcion para borrar los datos
#Funcion para el evento del click de los botones
def borrar():
    entrada.delete(0, tk.END)

def clickBoton(valor):
    entrada.insert(tk.END,valor)
#def calcular():
    #

#Crear la ventana principal
ventana=tk.Tk()
ventana.title("Calculadora")
ventana.geometry("308x500")

#Crear las entradas de datos
entrada=tk.Entry(ventana, font=("Roboto",30))
entrada.grid(row=0,column=3, pady=100)
entrada.configure(width=3)
#entrada.pack(fill="both",expand=True)
#entrada.configure(width=200)

#Crear los botones de la calculadora
botones=[
    '7','8','9','/',
    '4','5','6','x',
    '1','2','3','-',
    '0',',','=','+'
]
fila=1
columna=0

for boton in botones:
    btn=ttk.Button(ventana,text=boton, style="TButton")
    btn.grid(row=fila,column=columna)
    columna +=1
    if columna>3:
        columna=0
        fila +=1

#Estilos para el boton
estilo=ttk.Style()
estilo.configure("TButton", font=("Roboto", 16),background='#333',foreground="black", width=4, padding=10)

ventana.mainloop()
