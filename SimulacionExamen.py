#Simulacion Examen Parcial  
# Variables - Tipos de Datos - Entrada de Datos - Operadores
# 1. Crear 3 variables tipo numerico decimal y realizar la suma de los datos, el resultado multiplicarlo por un numero solicitado por teclado.
print("*** Crear 3 variables tipo numerico decimal y realizar la suma de los datos, el resultado multiplicarlo por un numero solicitado por teclado.***")
numero1=12.45
numero2=45.12
numero3=3.78
resultado=numero1+numero2+numero3
numero4=float(input("Ingrese un numero: "))
resultadoFinal=resultado*numero4
print("El resultado de la suma de ",numero1, " + ", numero2, " + ", numero3, "=",resultado)
print("Y la multiplicacion del Resultado de la suma de los 3 numeros ", resultado, " x ", numero4, "=",resultadoFinal )

#Tipos de Datos - Entrada de Datos - Condicionales
#2. Solicitar al usuario ingresar 2 numeros y determinar cual numero es el mayor
print("***Solicitar al usuario ingresar 2 numeros y determinar cual numero es el mayor***")
num1=float(input("Ingrese un Numero: "))
num2=float(input("Ingrese un Numero: "))
if num1>num2:
    print("El numero mayor es ",num1)
else:
    print("El numero mayor es ",num2)

#3. Solicitar al usuario ingresar 1 numero y determinar si es par o impar
print("Ejercicio 3 - Solicitar al usuario ingresar 1 numero y determinar si es par o impar") 
a=int(input("Ingrese un numero: "))
if a%2==0:
    print("El numero ", a, " es par")
else:
    print("El numero ", a, " es impar")

#varibales compuestas Listas - metodos de las listas
#4. Crear una lista 5 numeros y determinar el valo maximo y el valor minimo de la lista
print("Ejercicio 4- Crear una lista 5 numeros y determinar el valo maximo y el valor minimo de la lista")
listaNumero=[4,12.5,85,93.6,7]
print("El valor maximo de la lista es: ",max(listaNumero))
print("El valor minimo de la lista es: ",min(listaNumero))
#5. Crear una lista vacia, y solicitar al usuario ingresar 5 numero a la lista por teclado
print("Crear una lista vacia, y solicitar al usuario ingresar 5 numeros a la lista por teclado")
listaVacia=[]
n1=float(input("Ingrese un numero: "))
listaVacia.append(n1)
n2=float(input("Ingrese un numero: "))
listaVacia.append(n2)
n3=float(input("Ingrese un numero: "))
listaVacia.append(n3)
n4=float(input("Ingrese un numero: "))
listaVacia.append(n4)
n5=float(input("Ingrese un numero: "))
listaVacia.append(n5)
print("La lista nueva es: ", listaVacia)

#6. Con los datos del ejercicio numero 5 realizar la suma de los diferente elementos de la lista 
sumaListaVacia=sum(listaVacia)
print("La suma de los numeros de la lista ", listaVacia, " es: ",sumaListaVacia)


#7. Crear una lista de COLORES (azul,verde,amarillo,rojo,lila) y mostrar en pantalla el color rojo
print("Crear una lista de COLORES (azul,verde,amarillo,rojo,lila) y mostrar en pantalla el color rojo")
colores=["azul","verde","amarillo","rojo","lila"] #Posiciones de los elementos de la lista se maneja des de0
print(colores[3])


#bucles - Iterativos - Repetitivos
#8. Bucles Iterativos for. Generar la lista de los numeros del 1 al 20
for i in range(1,21):
    print(i)
#9. Bucles Repetitivos while. Generar la tabla de multiplicar del 9
n=9
i=1
while i<=10:
    resultado=n*i
    print(n, "x",i,"=",resultado)
    i=i+1
#10. bucles repetivos condicionados - Crer un menu para un calculadora basica que permita sumar, restar, multiplicar y divir 2 numero ingresados por teclado

while True:
    opcion=int(input("Desea seguir utilizando la calculadora? 1. Para continuar 2. Para Salir: "))
    if opcion==1:
        print("***CALCULADORA BASICA***")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICAR")
        print("4. DIVIDIR")
        opcionCalculadora=int(input("Elija la operacion a realizar: "))
        nm1=float(input("Ingrese un numero: "))
        nm2=float(input("Ingrese un numero: "))
        if opcionCalculadora==1:
            resultado=nm1+nm2
            print("El resultado de la suma ",nm1, "+",nm2,"=",resultado)
        elif opcionCalculadora==2:
            resultado=nm1-nm2
            print("El resultado de la resta ",nm1, "-",nm2,"=",resultado)
        elif opcionCalculadora==3:
            resultado=nm1*nm2
            print("El resultado de la multiplicacion ",nm1, "x",nm2,"=",resultado)
        elif opcionCalculadora==4:
            resultado=nm1/nm2
            print("El resultado de la division ",nm1, "/",nm2,"=",resultado)
        else:
            print("Error Operacion no Valida")
    elif opcion==2:
        break
    else:
        print("Error operacion no valida")

#Funciones
#11. Crear una funcion para sumar 2 numeros
def sumarNumero(x,y):
    resultado=x+y
    print("La suma de ",x,"+",y,"=",resultado)


sumarNumero(4,5)
sumarNumero(12.55,9)
sumarNumero(8,665.52)
sumarNumero(num1,num2)

#Tkinter - visual




