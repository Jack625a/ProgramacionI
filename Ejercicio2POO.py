#Ejercicio de clase - 3 de agosto
#Crear una clase para el manejo de Cajero Automatico
#En el cual se pueda depositar dinero, retirar dinero, ver saldo
#Tambien la clase debera poder almacenar diferentes cuentas
#(Nombre,Saldo,contraseña)

class Cajero:
    #Paso 1 -Definir los Parametros o atributos
    def __init__(self,nombre,saldo,contraseña):
        self.nombre=nombre
        self.saldo=saldo
        self.contraseña=contraseña

    #Paso 2 - Definir los metodos o acciones 
    #Accion 1 - Depositar dinero a la cuenta
    def depositar(self):
        cantidad=float(input("Ingrese la cantidad de dinero a depositar: "))
        self.saldo+=cantidad
        print("Se ha depositado ",cantidad,"Bs", "en la cuenta de ",self.nombre, " su saldo actual es ",self.saldo)
    
    #Accion 2 - Retirar dinero de la cuenta
    def retirar(self):
        cantidad=float(input("Ingrese la cantidad de dinero a retirar: "))
        if self.saldo>=cantidad:
            self.saldo-=cantidad
            print("Se ha retirado correctamente ",cantidad,"Bs"," de la cuenta de",self.nombre, " su saldo actual es ",self.saldo)
            return cantidad
        else:
            print("Error, Saldo insuficiente en la cuenta de ",self.nombre)
            return 0
    #Accion 3 - Ver Saldo
    def verSaldo(self):
         print("Bienvenido ",self.nombre, " su saldo disponible es ",self.saldo,"Bs")
    
#Paso 3 - Definir los objetos de la clase
cuenta1=Cajero("Kevin Arroyo Montaño",1000,"123")#objetos
cuenta2=Cajero("Felix Paye",1500,"456")
cuenta3=Cajero("Ernesto Acha",1800,"789")
cuenta4=Cajero("Alexia Villegas",1300,"741")
cuenta5=Cajero("Herber Paredez",1800,"852")
cuenta6=Cajero("Ismael Mondaque",1700,"963")
cuenta7=Cajero("Praxides Camata",1900,"369")
cuenta8=Cajero("Wilder Quispe",1240,"147")

#Crear la funcion principal para la autentificacion de los clientes
print("Bienvenido al cajero automatico")
contraseña=input("Ingrese su contraseña: ")
if contraseña==cuenta1.contraseña:
    cuenta=cuenta1
elif contraseña==cuenta2.contraseña:
    cuenta=cuenta2
elif contraseña==cuenta3.contraseña:
    cuenta=cuenta3
elif contraseña==cuenta4.contraseña:
    cuenta=cuenta4
elif contraseña==cuenta5.contraseña:
    cuenta=cuenta5
elif contraseña==cuenta6.contraseña:
    cuenta=cuenta6
elif contraseña==cuenta7.contraseña:
    cuenta=cuenta7
elif contraseña==cuenta8.contraseña:
    cuenta=cuenta8
else:
    print("Contraseña incorrecta")

#Mostrar la operaciones que puede realizar 
while True:
    print("Bienvenido seleccion la operación que desea realizar")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("0. Salir")
    opcion=int(input(">"))
    if opcion==1:
        cuenta.verSaldo()
    elif opcion==2:
        cuenta.depositar()
    elif opcion==3:
        cuenta.retirar()
    elif opcion==0:
        print("Gracias hasta pronto....")
        break
    else:
        print("Operación invalida")