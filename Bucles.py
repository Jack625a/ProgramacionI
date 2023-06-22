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






#BUcles Iterativos
