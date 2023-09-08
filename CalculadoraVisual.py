#Ejercicio 1- 07/09/2023
#Funcion para una calculadora simple con Tkinter
#SUMAR - RESTAR - MULTIPLICAR - DIVIDIR
#Paso 1 - Importar las librerias
import tkinter as tk
from tkinter import ttk #Importar ttk de tkinter para los estilos

#Paso 2 -Crear la funcion para la calculadora
def calcular():
    numero1=float(entry_numero1.get())
    numero2=float(entry_numero2.get())
    operacion=operacion_variable.get()

    if operacion=="Sumar":
        resultado.set(numero1+numero2)
    elif operacion=="Restar":
        resultado.set(numero1-numero2)
    elif operacion=="Multiplicar":
        resultado.set(numero1*numero2)
    elif operacion=="Dividir":
        if numero2!=0:
            resultado.set(numero1/numero2)
        else:
            resultado.set("Error no es posible dividir por cero..")
    
#Paso 3. Creacion del aspecto visual
#Paso 3.1 Crear la ventana
ventana=tk.Tk()
ventana.title("Calculadora Simple")
#Estilos
estilo=tk.ttk.Style()
estilo.configure('TButton',padding=10, font=('Calibri',15), bg="red")

#Paso 3.2. Entradas de datos - (Entry =>Tkinter)
entry_numero1=tk.Entry(ventana,width=10)
entry_numero1.grid(row=0,column=0, padx=10,pady=10)
entry_numero2=tk.Entry(ventana,width=10)
entry_numero2.grid(row=0,column=2,padx=10,pady=10)

#Paso 3.3 Operaciones (OptionMenu)

opereraciones=["Sumar","Restar","Multiplicar","Dividir"] #Lista de las operaciones (suma, resta, multiplicacion, division)
operacion_variable=tk.StringVar()
operacion_variable.set(opereraciones[0])# Valor predeterminado
menu_operaciones=tk.OptionMenu(ventana, operacion_variable, *opereraciones)
menu_operaciones.grid(row=0, column=1,padx=10,pady=10)

#Paso 3.4 Creacion de Boton de calcular (Button)
calcular_boton=tk.Button(ventana, text="Calcular",command=calcular,font=('Calibri',15,'bold'), background="red")
calcular_boton.grid(row=1,column=1)

#Paso 3.5 Mostrar el Resultado en Pantalla (Label)
resultado=tk.StringVar()
resultado.set("")
titulo_resultado=tk.Label(ventana,text="Resultado: ",font=('Calibri',15,'bold'))
titulo_resultado.grid(row=2,column=0, padx=10,pady=10)
resultado_texto=tk.Label(ventana,textvariable=resultado,font=('Calibri',15,'bold'))
resultado_texto.grid(row=2,column=1, padx=10,pady=10)

#Paso 4. Crear en enfoque a la ventana
ventana.mainloop()

