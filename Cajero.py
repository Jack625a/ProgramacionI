#Interfaz grafica en Tkinter - Python
#12-10-2023
#Ejercicio 1 - Crear un cajero automatico (ver saldo, depositar, retirar)

#PASO 1 IMPORTACION DE LOS MODULOS PARA EL ASPECTO VISUAL
import tkinter as tk #Tkinter para el ASPECTO VISUAL
from tkinter import messagebox #mensajes

#PASO 2 - DEFINIR LOS DATOS DE LOS USUARIOS (USUARIO, CONTRASEÑA, NOMBRE SALDO)
usuarios={
    "usuario1":{
        "contraseña":"12345",
        "nombre":"Kevin Arroyo",
        "saldo":1500
                },
    "usuario2":{
        "contraseña":"7894",
        "nombre":"Ernesto Acha",
        "saldo":1900
                },
    "usuario3":{
        "contraseña":"7412",
        "nombre":"Camilo Mamani",
        "saldo":1506
                },
    "usuario4":{
        "contraseña":"8523",
        "nombre":"Felix Paye",
        "saldo":1600
                },
    "usuario5":{
        "contraseña":"9633",
        "nombre":"Withzarely Escobar",
        "saldo":1800
                },
            
}
#PASO 3. Definir las funciones para el programa
#Funcion 1. Verificar Contraseña
#Funcion 2. Depositar
#Funcion 3. Retirar
#Funcion 4. Ver saldo

def verificar():
    #CONECTAMOS CON EL TKINTER - Metodo GET
    usuario=usuario_entry.get()
    contraseña=contraseña_entry.get()
    if usuario in usuarios and usuarios[usuario]["contraseña"]==contraseña:
        print("Bienvenido")
        messagebox.showinfo("Bienvenido")
        menu_frame.pack()
        login_frame.pack_forget()
    else:
        messagebox.showerror("Error Usuario o Contraseña incorrectos")


#Funcion para deposito de dinero a la cuenta
def depositar():
    usuario=usuario_entry.get()
    monto=int(monto_entry.get())
    usuarios[usuario]["saldo"]+=monto
    saldo_label.config(text=f"Saldo: Bs {usuarios[usuario]['saldo']}")
    monto_entry.delete(0, tk.END)

#Funcion para retiro de dinero de la cuenta
def retirar():
    usuario=usuario_entry.get()
    monto=int(monto_entry.get())

    if monto<=usuarios[usuario]["saldo"]:
        usuarios[usuario]["saldo"]-=monto
        saldo_label.config(text=f"Salado: Bs{usuarios[usuario]['saldo']}")
        monto_entry.delete(0,tk.END)
    else:
        messagebox.showerror("Error","Saldo Insuficiente")

def versaldo():
    usuario=usuario_entry.get()
    saldo_label.config(text=f"Saldo Actual: Bs{usuarios[usuario]['saldo']} - Usuario: {usuarios[usuario]['nombre']}", font="'Calibri',20")
#Paso 4. Crear el aspecto visual
#Crear la ventana Principal
ventana=tk.Tk()
ventana.title("Cajero Automatico")
#Crear el frame 
#FRAME PARA EL INICIO DE SESION
login_frame=tk.Frame(ventana)
menu_frame=tk.Frame(ventana)

#Componentes para el frame de inicio de sesion
usuario_label=tk.Label(login_frame, text="Usuario: ")
usuario_entry=tk.Entry(login_frame)
contraseña_label=tk.Label(login_frame, text="Contraseña: ")
contraseña_entry=tk.Entry(login_frame,show="*")
#Boton para conecta con la funcion VERIFICAR
botonlogin=tk.Button(login_frame, text="Iniciar Sesión", command=verificar)
#Posicionar los componentes
usuario_label.pack()
usuario_entry.pack()
contraseña_label.pack()
contraseña_entry.pack()
botonlogin.pack()

#Crear los componentes para el frame del menu
saldo_label=tk.Label(menu_frame,text="")
monto_label=tk.Label(menu_frame,text="Monto: ")
monto_entry=tk.Entry(menu_frame)
botondepositar=tk.Button(menu_frame,text="Depositar",command=depositar)
botonretirar=tk.Button(menu_frame,text="Retirar", command=retirar)
botonVerSaldo=tk.Button(menu_frame,text="Ver Saldo", command=versaldo)

saldo_label.pack()
monto_label.pack()
monto_entry.pack()
botondepositar.pack()
botonretirar.pack()
botonVerSaldo.pack()

#Mostrar el frame de inicio de sesion 
login_frame.pack()
ventana.mainloop()