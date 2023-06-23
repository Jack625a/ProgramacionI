#Bucles,
#Bucles Condicionales Repetitivo
#1. Bucles Repetitivos Condicionados
#while condicion:
# //Codigo
print("Ejercicio 1. Mostrar los primeros numeros del 1 al 10")
#Ejercicio 1. Mostrar los primeros numeros del 1 al 10
numero=1
while numero<=100:
    print(numero)
    numero=numero+1

print("Ejercicio 2. Mostrar los numeros del 100 al 1")
#Ejercicio 2. Mostrar los numeros del 100 al 1
numero2=100
while numero2>=1:
    print(numero2)
    numero2=numero2-1


#2. Bucles Repetitivos Logicos
#while True:
#if condicion:
#break=> False


#Ejercicio 3
productos=[]
while True:
    opcion=input("Desea agregar productos a la tienda? Si para continuar, No paras salir:  ")
    if opcion=="Si":
        agregar_producto=input("Ingrese el nombre del producto: ")
        productos.append(agregar_producto)
    elif opcion=="No":
        print("Se agregaron correctamente los productos a la tienda ", productos)
        break 
    else:
        print("Error operacion no valida")

#BUcles Iterativos
#FOR
#for i range(1,20)
#Ejercicio 4- Mostrar los primeros numeros del 1 al 10 con el ciclo for
print("Ejercicio 4- Mostrar los primeros numeros del 1 al 10 con el ciclo for")
for n in range(1,11):
    print(n)
#Ejercicio 5 - Mostrar los numeros pares del 1 al 100
print("Ejercicio 5 - Mostrar los numeros pares del 1 al 100")
for p in range(0,101,2):
    print(p)
#Ejercicio 6 - Mostrar los numeros impares del 1 al 100
print("Numeros Impares")
for i in range(1,101):
    #Verificacion si el numero es impar
    if i%2 !=0:
        print("Numero impar",i)
    else:
        print("Numero par: ",i)

#Ejercicio 7 - Combinacion de Bucles y Condicionales
productos=[]
while True:
    opcion=input("Desea agregar productos a la tienda? Si para continuar, No paras salir:  ")
    if opcion=="Si":
        cantidad_productos=int(input("Cuanto productos agregara a la tienda?"))
        for producto in range(1,cantidad_productos+1):
            agregar_producto=input("Ingrese el nombre del producto: ")
            productos.append(agregar_producto)
    elif opcion=="No":
        print("Se agregaron correctamente los productos a la tienda ", productos)
        break 
    else:
        print("Error operacion no valida")

