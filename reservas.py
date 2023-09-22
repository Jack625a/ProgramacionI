#Ejercicio 1 - 21/09/2023
#Crear un sistema de reservas para un Hotel.
#Importar las librerias a utilizar
import tkinter as tk
from tkinter import ttk
#pip install tkcalendar
from tkcalendar import DateEntry #Biblioteca de calendario - (fecha)
#Notificaciones Emergentes
from tkinter import messagebox

#PASO 1- ALMACENAMIENTO DE RESERVAS - LISTA 
reservas=[]
#PASO 2 - CREAR LA FUNCION PARA REALIZAR UNA RESERVA
def realizarReserva():
    nombre=entryNombre.get()
    habitacion=entryHabitacion.get()
    fechaEntrada=entryFEntrada.get_date()
    fechaSalida=entryFSalida.get_date()

    if nombre and habitacion and fechaEntrada and fechaSalida:
        reservas.append((nombre,habitacion,fechaEntrada,fechaSalida))
        actualizarReserva()
        messagebox.showinfo("Reservas Exitosa: ",f"Nombre: {nombre} para la habitacion numero {habitacion} con fecha de entrada {fechaEntrada} y fecha de salida {fechaSalida}.")
    else:
        messagebox.showerror("Error complete todos los datos para continuar...")

#Recordatorio de las lista y sus metodos
#lista=[1,2,3,4,5,66,88,99,77,82,16]
#resultado=5
#resultado=88
#respuesta=print(lista)

#PASO 3 - CREAR UN FUNCION PARA ACTUALIZAR LA LISTA DE LAS RESERVAS
def actualizarReserva():
    listaReserva.delete(0, tk.END)
    #Iteracion de los elemento de la lista de reservas
    for reserva in reservas:
        listaReserva.insert(tk.END, f"{reserva[0]} - Habitacion: {reserva[1]} - Fecha de Entrada: {reserva[2]} - Fecha de Salida: {reserva[3]}")

#PASO 4 - CREAR LA VENTANA PRINCIPAL 
ventana=tk.Tk()
ventana.title("Sistema de Reservas Hotel ABC")
#TituloPrincipal
titulo=tk.Label(ventana, text="Sistema de Reservas Hotel ABC", font=('Calibri', 18))
titulo.grid(row=0,column=1)
#Paso 4.1 Entrada y titulos para el ingreso de datos (Formulario)
tituloNombre=tk.Label(ventana, text="Nombre:  ")
tituloNombre.grid(row=1,column=0)
entryNombre=tk.Entry(ventana)
entryNombre.grid(row=1,column= 1)
tituloHabitacion=tk.Label(ventana, text="Habitación:  ")
tituloHabitacion.grid(row=2,column=0)
entryHabitacion=tk.Entry(ventana)
entryHabitacion.grid(row=2,column=1)

#Fechas - libreria de calendario
tituloFechaEntrada=tk.Label(ventana, text="Fecha de Entrada: ")
tituloFechaEntrada.grid(row=3,column=0)
entryFEntrada=DateEntry(ventana, width=15, background='darkblue',foreground='white', font=('Calibri',12))
entryFEntrada.grid(row=3,column=1)
tituloFechaSalida=tk.Label(ventana, text="Fecha de Salida: ")
tituloFechaSalida.grid(row=4,column=0)
entryFSalida=DateEntry(ventana,width=15, background='darkblue',foreground='white',font=('Calibri',12))
entryFSalida.grid(row=4,column=1)

#CREAR EL BOTON DEL FORMULARIO
reservarBoton=tk.Button(ventana,text="Realizar Reserva", command=realizarReserva, font=('Calibri',13))
reservarBoton.grid(row=5,column=1)


#Mostrar la lista de las reservas
listaReserva=tk.Listbox(ventana,font=('Calibri',13))
listaReserva.grid(row=6,column=1)





ventana.mainloop()