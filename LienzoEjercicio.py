#
import tkinter as tk

#Varibales para almacenar la poscion del raton
prev_x=0
prev_y=0

#funcion para dibujar
def dibujar(event):
    global prev_x, prev_y
    #Obtener las posiscion actual del mouse.
    x=event.x
    y=event.y
    lienzo.create_line(prev_x,prev_y,x,y, fill="red",width=2)
    #Actualizar la posicion anterior
    prev_x=x 
    prev_y=y

#fUNCION PARA RESETEAR LA POSICION
def resetearPosicion(event):
    global prev_x,prev_y
    #Restablcer su posicion 
    prev_x=event.x
    prev_y=event.y

#Funcion para resetear el lienzo
def borrarLienzo(event):
    lienzo.delete("all")


##Interfaz grafica

ventana=tk.Tk()
ventana.title("Lienzo")
lienzo=tk.Canvas(ventana,width=400,height=400)
lienzo.pack()

#Conectar los eventos del mouse 
lienzo.bind("<B1-Motion>",dibujar) #DIBUJAR LINEAS AL PRESIONAR EL BOTON IZQUIERDO DEL MOUSE
lienzo.bind("<Button-1>",resetearPosicion)
lienzo.bind("<Button-3>",borrarLienzo)



ventana.mainloop()