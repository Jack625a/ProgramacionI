import tkinter as tk

ventana=tk.Tk()
lienzo=tk.Canvas(ventana, width=300,height=300)
lienzo.pack()


#Dibujar una linea
lienzo.create_line(0,0,150,150,fill="blue",width=3)
#Dijuar circulo
lienzo.create_oval(100,100,250,250,fill="green")
#Dibujar Rectangulo
lienzo.create_rectangle(50,50,200,200, fill="red")
lienzo.create_text(150,100,text="ProgramacionI",fill="blue",font=("Arial",20))

ventana.mainloop()