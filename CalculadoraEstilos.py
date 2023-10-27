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

def calcular():
    try:
        resultado=eval(entrada.get())
        entrada.delete(0,tk.END)
        entrada.insert(0,str(resultado))
    except Exception:
        entrada.delete(0,tk.END)
        entrada.insert(0,"Error")

#Crear la ventana principal
ventana=tk.Tk()
ventana.title("Calculadora")
ventana.geometry("308x500")

pantalla1=tk.Frame(ventana, bg="white", height=200 )
pantalla1.pack(fill="both", expand=True)

pantalla2=tk.Frame(ventana, bg="white")
pantalla2.pack(fill="both",expand=True)

#Crear las entradas de datos
entrada=tk.Entry(pantalla1, font=("Roboto",30))
#entrada.grid(row=0,column=3, pady=100)
#entrada.configure(width=2)
entrada.pack(fill="both",expand=True, pady=95)



#Crear los botones de la calculadora
botones=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','+',
    
]

botones2=[
    'C','=','','',
]


fila=1
columna=0

for boton2 in botones2:
    if boton2=="=":
        ttk.Button(pantalla2,text=boton2, style="TButton",command=calcular ).grid(row=fila,column=columna)
    elif boton2=="C":
        ttk.Button(pantalla2, text=boton2, style="TButton",command=borrar ).grid(row=fila, column=columna)
    else:
        ttk.Button(pantalla2, text=boton2,style="TButton").grid(row=fila,column=columna)
    columna +=1
    if columna>3:
        columna=0
        fila +=1

#Estilos para el boton
estilo=ttk.Style()
estilo.configure("TButton", font=("Roboto", 16),background='#333',foreground="black", width=4, padding=10)


#ASIGNACION DE FUNCIONES A LOS BOTONES
for boton in botones:
    ttk.Button(pantalla2, text=boton, style="TButton", command=lambda a=boton:clickBoton(a)).grid(row=fila,column=columna)
    columna+=1
    if columna>3:
        columna=0
        fila+=1

#Configuracion de entrada de dato
#for i in range(4):
 #   ventana.grid_rowconfigure(i, weight=1)
  #  ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()
