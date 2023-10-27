import tkinter as tk

ventana=tk.Tk()

pantalla1=tk.Frame(ventana, bg="green", height=200 )
pantalla1.pack(fill="both", expand=True)

pantalla2=tk.Frame(ventana, bg="red",height=200)
pantalla2.pack(fill="both",expand=True)

ventana.mainloop()