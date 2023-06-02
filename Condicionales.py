#Condicionales en Python
#if condicion:
#bloque de codigo
#else:
#bloque de codigo
#Ejercicio 1 - Verificar el numero mayor de 2 numeros
print("Ejercicio 1 - Verificar el numero mayor de 2 numeros")
#Asignacion de las 2 variables 
#Mejora a la entrada de datos

a=int(input("Ingrese un numero: "))
b=float(input("Ingrese un numero: "))
if a>b:
    print("El numero mayor es:",a)
elif a==b:
    print("Los dos numeros son iguales")
else:
    print("El numero mayor es:",b)

#Entrada de datos por teclado
#input=> Cadena de cadena de caracteres 
#Ejercicio 2 - VERIFICAR EL MAYOR DE 3 NUMEROS
print("Ejercicio 2 - VERIFICAR EL MAYOR DE 3 NUMEROS INGRESADOS POR TECLADO")
#Paso 1 - DEFINIR LAS VARIABLES CON ENTRADA DE DATOS NUMERICO - DECIMALES Y ENTEROS=> FLOAT
num1=float(input("Ingrese un numero"))
num2=float(input("Ingrese un numero"))
num3=float(input("Ingrese un numero"))
#caso 1
#num1=25 - num2=12 - num3=13
#caso 2
#num1=25 - num2=12 - num3=45
#caso 3
##num1=25 - num2=30 - num3=13
#caso 4
#num1=25 - num2=30 - num3=45
#Paso 2- Ingresar la condicion
if num1>num2:
    if num1>num3:
        print("El numero mayor es: ",num1)
    else:
        print("El numero mayor es: ",num3)
else:
    if num2>num3:
        print("El numero mayor es: ",num2)
    else:
        print("El numero mayor es ",num3)

