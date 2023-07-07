import math
#Funciones Lambda para operadores Aritmeticos
suma=lambda a,b:a+b
resta=lambda a,b:a-b
multiplicacion=lambda a,b:a*b
division=lambda a,b:a/b
seno=lambda r:math.sin(r)
coseno=lambda r:math.cos(r)
tangente=lambda r:math.tan(r)

def sumar(num1,num2):
    resultado=num1+num2
    return resultado

def Calculadora():
    print("Caculadora - Programación I")
    print("Seleccione una Opción")
    print("1. Operaciones Aritmeticas")
    print("2. Operaciones Trigonometricas")
    print("3. Operaciones Geometricas")
    print("4. Operaciones Logaritmitcas")

    opcion=int(input("Ingrese la opcion: "))

    if opcion==1:
        print("Seleccione una operacion aritmetica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        operacion=int(input("Ingrese la operacion que desea realizar: "))
        #Valores de entrada para el calculo de la operacion
        numero1=float(input("Ingrese un numero: "))
        numero2=float(input("Ingrese un numero: "))
        if operacion==1:
            resultado=suma(numero1,numero2)



while True:
    continuar=input("Desea continuar con la calculadora? Si para continuar, No para Salir: ")
    if continuar=="Si":
        print("Caculadora - Programación I")
        print("Seleccione una Opción")
        print("1. Operaciones Aritmeticas")
        print("2. Operaciones Trigonometricas")
        print("3. Operaciones Geometricas")
        print("4. Operaciones Logaritmitcas")

        opcion=int(input("Ingrese la opcion: "))

        if opcion==1:
            print("Seleccione una operacion aritmetica")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            operacion=int(input("Ingrese la operacion que desea realizar: "))
            #Valores de entrada para el calculo de la operacion
            numero1=float(input("Ingrese un numero: "))
            numero2=float(input("Ingrese un numero: "))

            #Condicional para verificar cual operacion se realiazara
            if operacion==1:
                resultado=numero1+numero2
                print("El resultado de la suma de ",numero1,"+",numero2,"=",resultado)
            elif operacion==2:
                resultado=numero1-numero2
                print("El resultado de la resta de ",numero1,"-",numero2,"=",resultado)
            elif operacion==3:
                resultado=numero1*numero2
                print("El resultado de la multiplicacion de ",numero1,"x",numero2,"=",resultado)
            elif operacion==4:
                resultado=numero1/numero2
                print("El resultado de la division de ",numero1,"/",numero2,"=",resultado)
            else:
                print("Error operacion no valida")

        elif opcion==2:
            print("Seleccione una operacion trigonometrica")
            print("1. Seno")
            print("2. Coseno")
            print("3. Tangente")
            operacion=int(input("Ingrese la opcion que desea realizar: "))
            angulo=float(input("Ingrese el angulo: "))

            #Condicional para la seleccion de las opciones
            if operacion==1:
                resultado=math.sin(angulo)
                print("El resultado del seno del angulo",angulo," es ",resultado)
            elif operacion==2:
                resultado=math.cos(angulo)
                print("El resultado del coseno del angulo",angulo," es ",resultado)
            elif operacion==3:
                resultado=math.tan(angulo)
                print("El resultado de la tangente del angulo",angulo," es ",resultado)
            else:
                print("Error operacion no validad")
        elif opcion==3:
            print("Seleccione una operacion geometrica")
            print("1. Area del circulo")
            print("2. Area del triangulo")
            print("3. Area del rectangulo")
            operacion=int(input("Ingrese la operacion a realizar: "))

            if operacion==1:
                radio=float(input("Ingrese el radio del circulo: "))
                resultado=math.pi*radio**2
                print("El area del circulo es: ",resultado)
            elif operacion==2:
                base=float(input("Ingrese la base del triangulo: "))
                altura=float(input("Ingrese la altura del triangulo: "))
                resultado=(base*altura)/2
                print("El area del triagulo es: ",resultado)
            elif operacion==3:
                base=float(input("Ingrese la base del rectangulo: "))
                altura=float(input("Ingrese la altura del rectangulo: "))
                resultado=base*altura
                print("El area del rectangulo es: ", resultado)
            else:
                print("Error operacion no valida")
        elif opcion==4:
            print("Seleccione una operacion logaritmica")
            print("1. Logaritmo en base 10")
            print("2. Logaritmo en base 2")
            print("3. Logaritmo Natural")
            operacion=int(input("Ingres la operacion que desea realizar: "))
            #Condicional
            numero=float(input("Ingrese un numero"))
            if operacion==1:
                resultado=math.log10(numero)
                print("El logaritmo en base 10 de ",numero, "es:", resultado)
            elif operacion==2:
                resultado=math.log2(numero)
                print("El logaritmo en base 2 de ",numero, "es:", resultado)
            elif operacion==3:
                resultado=math.log(numero)
                print("El logaritmo natural de ",numero, "es:", resultado)
            else:
                print("Error Operacion no valida")
        else:
            print("Error opcion no valida")
    elif continuar=="No":
        print("Gracias por utilizar la calculadora...")
        break 
    else:
        print("Error opcion no valida")           
