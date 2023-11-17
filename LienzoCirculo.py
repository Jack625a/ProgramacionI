import tkinter as tk

#Funcion para mover el ciruclo al seguir al mouse
def mover(event):
    lienzo.coords(imagen,event.x-25,event.y-25)


ventana=tk.Tk()
lienzo=tk.Canvas(ventana,width=500,height=500)
lienzo.pack()

imagen=tk.PhotoImage(file="mario3.png")

#IMAGEN INSERTADA EN EL LIENZO
lienzo.create_image(0,0,anchor=tk.NW, image=imagen)

#Conectar la funcion al moviento del raton con el circulo
lienzo.bind("<Motion>",mover)

ventana.mainloop()