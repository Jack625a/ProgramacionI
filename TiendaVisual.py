#Ejercicio 1 - 14-09-2023
#Crear una tienda simple que permita agregar productos y realizar ventas
#PASO 1. IMPORTAR LAS LIBRERIAS A UTILIZAR
import tkinter as tk
#PASO 2. CREAR LA FUNCION PARA AGREGAR UN PRODUCTO A LA TIENDA
def agregar_producto():
    producto=entry_producto.get()
    precio=float(entry_precio.get())
    lista_productos.insert(tk.END, f"Producto: {producto} - Bs{precio:.2f}")

#PASO 3. Funcion para vender un producto
def vender_producto():
    seleccion=lista_productos.curselection() #Obtenemos la seleccion del producto
    if seleccion:
        producto_vendido=lista_productos.get(seleccion)
        venta_lista.insert(tk.END, producto_vendido)

#PASO 4. CREAR LA INTERFAZ GRAFICA 
#PASO 4.1. CREAR LA VENTANA PRINCIPLA
ventana=tk.Tk()
ventana.title("TIENDA BASICA PROGRAMACION I")
#PASO 4.2. CREAR LOS COMPONENTES PARA AGREGAR PRODUCTOS 
#ENTRADA DE DATOS: 2 ENTRY
#TEXTO: 2 LABEL
tituloAgregar=tk.Label( ventana,text="Agregar Productos",font=('Impact',18))
tituloAgregar.grid(row=0,column=1, pady=15, padx=30)
label_producto=tk.Label(ventana, text="Producto: ",font=('Calibri',16))
#Posicionar el componente (1.pack 2. grid 3.place )
label_producto.grid(row=1,column=0)
#Entrada de datos
entry_producto=tk.Entry(ventana)
entry_producto.grid(row=1,column=1)

#Precio
label_precio=tk.Label(ventana, text="Precio: ",font=('Calibri',16))
label_precio.grid(row=2,column=0)
entry_precio=tk.Entry(ventana)
entry_precio.grid(row=2,column=1)

#BOTON PARA AGREGAR PRODUCTO
boton=tk.Button(ventana, text="Agregar Producto", command=agregar_producto,background="blue",font=('Calibri',13))
boton.grid(row=3,column=1)

#LISTA DE LOS PRODUCTOS DISPONIBLES EN LA TIENDA
titulo_productos=tk.Label(ventana,text="Productos Disponibles",font=('Impact',18))
titulo_productos.grid(row=4,column=1, pady=20)
lista_productos=tk.Listbox(ventana)
lista_productos.grid(row=5,column=1, padx=60)

#COMPONENTES PARA LA VENTA DE PRODUCTO DISPONIBLE
botonVender=tk.Button(ventana,text="Vender Producto",command=vender_producto, background="blue",font=('Calibri',13))
botonVender.grid(row=6,column=1, pady=20)

#Titulo de la lista de las ventas realizadas
tituloVentas=tk.Label(ventana,text="VENTAS REALIZADAS",font=('Impact',18))
tituloVentas.grid(row=7,column=1, pady=10)
#CREAR LA LISTA DE LAS VENTAS
venta_lista=tk.Listbox(ventana)
venta_lista.grid(row=8,column=1,pady=15)


ventana.mainloop()
