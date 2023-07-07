#CREACION DE LAS LISTAS 
productos=[] #Lista de los productos
usuarios=[] #Lista de los usuarios
carrito=[] #Lista de productos agregados al Carrito

#Funcion para Agregar Productos a la Tienda, (Nombre,Precio)
def agregar_producto(nombre,precio):
    #CREACION DEL DICCIONARIO PARA ALMACENAR LOS PRODUCTOS
    producto={"nombre":nombre,"precio":precio}
    #AGREGAR LOS PRODUCTOS A LA LISTA DE PRODUCTOS DE LA TIENDA
    #fUNCION APPEND PARA AGREGAR ELEMENTOS A UNA LISTA
    productos.append(producto)
    print("Producto agregado: ",producto["nombre"])

#Funcion para Agregar Usuarios a la Tienda. (Nombre, Contraseña)
def agregar_usuario(nombre,contraseña):
    usuario={"nombre":nombre,"contraseña":contraseña}
    usuarios.append(usuario)
    print("Usuario agregado: ",usuario["nombre"])

#Funcion para Mostrar los Productos de la Tienda
def mostrar_productos():
    print("Lista de Productos Disponibles")
    #Utilizar un ciclo iterativo para verificar los elementos de la lista Productps
    for producto in productos:
        print(producto["nombre"], "-",producto["precio"])

#Funcion para Mostrar los usuarios de la tienda
def mostrar_usuarios():
    print("Lista de Usuarios")
    for usuario in usuarios:
        print(usuario["nombre"])

#Funcion para Agregar un producto al Carrito de Compras
def agregar_al_carrito(producto):
    carrito.append(producto)
    print("Productos Agregado:", producto["nombre"])

#Funcion para Confirmar la compra de los Productos Agregados al Carrito
def realizar_compra():
    print("Productos en el Carrito de Compras")
    #Realizar una iteracion de los productos agregados al carrito
    for producto in carrito:
        print(producto["nombre"], "-", producto["precio"])
    print("Compra Realizada con exito!")
    #Utilizar la funcion para eliminar los elementos de la lista carrito
    carrito.clear()

#Funcion para el MENU del Admnistrador
def mostrar_menu_admin():
    while True:
        print("----Menu Administrador---")
        print("1. Agregar Productos a la tienda")
        print("2. Agregar Usuarios")
        print("3. Mostrar los Productos")
        print("4. Mostrar los clientes")
        print("5. Salir")

        opcion=int(input("Ingrese el numero de la opcion que desea realizar: "))
        if opcion==1:
            nombre=input("Ingrese el nombre del Producto: ")
            precio=float(input("Ingrese el precio del Producto: "))
            agregar_producto(nombre,precio)
        elif opcion==2:
            nombre=input("Ingrese el nombre completo del usuario: ")
            contraseña=input("Ingrese la contraseña del usuario: ")
            agregar_usuario(nombre,contraseña)
        elif opcion==3:
            mostrar_productos()
        elif opcion==4:
            mostrar_usuarios()
        elif opcion==5:
            print("Gracias por utlizar la sección del administrador...")
            break
        else:
            print("Opcion Invalida, ingrese una opcion validad del menu")

#Funcion del menu del usuarios
def mostrar_menu_comprador():
    while True:
        print("----Menu del Comprador----")
        print("1. Mostrar los Productos de la Tienda")
        print("2. Agregar Producto al Carrito")
        print("3. Realizar la Compra")
        print("4. Salir")
        opcion=int(input("Ingrese el numero de la opcion del menu que desea realizaer: "))
        if opcion==1:
            mostrar_productos()
        elif opcion==2:
            nombre_producto=input("Ingrese el nombre del producto que desea agregar al Carrito: ")
            producto_encontrado=None
            for producto in productos:
                if producto["nombre"]==nombre_producto:
                    producto_encontrado=producto
                    break
            if producto_encontrado:
                agregar_al_carrito(producto_encontrado)
            else:
                print("Producto no disponible en la tienda")
        elif opcion==3:
            realizar_compra()
        elif opcion==4:
            print("Gracias por comprar en nuestra tienda...")
            break
        else: 
            print("Error opcion invalida")

#Funcion Principal para iniciar la tienda
def iniciar_tienda():
    while True:
        print("----Tienda Online----")
        print("1. Menu del Administrador")
        print("2. Menu del Comprador")
        print("3. Salir")

        opcion=int(input("Ingrese la opcion que desea realizar: "))
        if opcion==1:
            contraseña=input("Ingrese la contraseña: ")
            if contraseña=="admin123":
                mostrar_menu_admin()
            else:
                print("Contraseña incorrecta. Acceso denegado")
        elif opcion==2:
            mostrar_menu_comprador()
        elif opcion==3:
            break
        else:
            print("Error opcion invalida")


#Iniciar la tienda
iniciar_tienda()
