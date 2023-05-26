#Listas
nombres=["Kevin","Alexia","Wilder","Ernesto","Herber","Fernando","Edgar"]
colores=["rojo","verde","cafe","azul","amarillo"]
#Acceder a un elemento de la lista
print("El primer nombre es: ", nombres[0])
print("El cuarto nombre es: ", nombres[3])
#Acceder al ultimo elemento de la lista
print("El ultimo nombre de la lista es: ",nombres[-1])
print("El ultimo color de la lista es: ", colores[-1])
#Acceder a un rango de elemento de la lista
#Ejemplo 1 - Acceder a los primeros 3 nombres de la lista "NOMBRES"
print("Ejemplo 1 - Acceder a los primeros 3 nombres de la lista NOMBRES")
print("Los 3 primeros nombres de la lista son: ",nombres[0:3])
#Ejercicio 2 - Acceder a los primeros 4 colore de la lisa "COLORES"
print("Ejercicio 2 - Acceder a los primeros 4 colore de la lisa COLORES")
print("Los 4 primeros colores de la lista son",colores[0:4])
#Modificar elementos de la lista
#Ejercicio - 3- Actualizar los tres primeros nombres de la lista
print("Ejercicio - 3- Actualizar los tres primeros nombres de la lista")
nombres[0]="Kevin Arroyo"
nombres[1]="Alexia Villegas"
nombres[2]="Wilder Quispe"
print(nombres)
#Modificar varios elemento de la lista
#Ejercicio 4- Actualizar los 4 ultimos nombres de la lista
print("Ejercicio 4- Actualizar los 4 ultimos nombres de la lista")
#Primer paso ACCEDER A LOS 4 ULTIMOS NOMBRES DE LA LISTA
nombres[3:7]=["Ernesto Acha","Herber Paredez","Fernando Flores","Edgar Ayzacayo"]
print(nombres)
#Añadir un elemento a la lista
#funcion para añadir elemento a la lista: append
nombres.append("Nelson Aguirre")
nombres.append("Hilaria Barra")
print(nombres)
#Añadir varios elementos a la lista
#funcion para añadir varios elementos a la lista:extend
#Ejercicio 5 - Añadir 4 nombres a la lista
print("Ejercicio 5 - Añadir 4 nombres a la lista")
nombres.extend(["Ibet Rocha","Cesar Encinas","Filomena Argollo","Demetrio Juri"])
print(nombres)
#Insertar un elemento en una posicion especifica
#funcion para insertar un elemento en una posicion especifica: insert
colores.insert(2,"rosado")
print(colores)
#Eliminar un elemento especifico de la lista
#funcion que nos permite eliminar un elemento de la lista: remove
print("Ejercicio 6 - Eliminar el color rosado de la lista COLORES")
colores.remove("rosado")
print(colores)
print("Ejercicio 7 - Eliminar el ultimo color de la lista COLORES")
#FUNCION PARA ELIMINAR EL ULTIMO ELEMENTO DE UNA LISTA:POP
colores.pop()
print(colores)
print("Ejercicio 8 - Eliminar un elemento en una posicion en especifico")
#funcion para eliminar un elemento en especifico es: del
del colores[0]
print(colores)

