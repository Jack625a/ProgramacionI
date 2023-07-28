#Crear una clase Animal
#1. Atributos o Parametros
#2. Acciones o Metodos 
#3. Objetos 

class Animal:
    #Paso 1. Definir los atributos
    #Metodo init 
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    #Paso2. Definir los metodos o Acciones
    def comer(self):
        print("El animal",self.nombre," esta comiendo")
    def caminar(self):
        print("El animal",self.nombre, " esta caminando")
    
#Paso 3 Creacion de los objetos 
perro=Animal("Pancho",4) #Primer Objeto 
gato=Animal("Paco",3)   #Segundo Objeto

perro.comer()
gato.caminar()

#Ejercicio 1- Crear la Clase Materia Programacion I
#PASO 1 - DEFINIR LOS ATRIBUTOS O PARAMETROS
#Nombre, Carrera, Edad, Ci, Correo (Estudiante, Docente)
#Paso 2 - DEFINIR LAS ACCIONES O METODOS 
#RevisarExamenes, DarExamen, Estudiar
#Paso 3 - DEFINIR LOS OBJETOS
#docente, 22 estudiantes

#PASO 1 - DEFINIR LOS ATRIBUTOS O PARAMETROS
#Nombre, Carrera, Edad, Ci, Correo (Estudiante, Docente)
class ProgramacionI:
    def __init__(self,nombre,carrera,edad,ci,correo):
        self.nombre=nombre
        self.carrera=carrera
        self.edad=edad
        self.ci=ci
        self.correo=correo
    #Paso 2 - DEFINIR LAS ACCIONES O METODOS 
    #RevisarExamenes, DarExamen, Estudiar
    def calificar(self,parcial1,parcial2,final):
        estudianteCalificar=input("Ingrese el nombre del estudiante: ")
        notafinal=(parcial1+parcial2+final)/3
        print("La nota Final del estudiante ", self.nombre, "es ",notafinal)
    def darExamen(self):
        print("Seleccione la respuesta correcta, ingrese el numero de la respuesta")
        print("Comando para inicializar un repositorio")
        print("1. git clone")
        print("2. git init")
        print("3. git add")
        print("4. git inicializar")
        nota=0
        opcion=int(input("Cual es la respuesta correcta: "))
        if opcion==2:
            print("Respuesta Correcta")
            nota=nota+50
        else:
            print("Respuesta incorrecta")
        
        
        print("Comando para crear Ramificaciones")
        print("1. git clone")
        print("2. git rama")
        print("3. git branch")
        print("4. git reverse")
        opcion2=int(input("Cual es la respuesta correcta: "))
        if opcion2==3:
            print("Respuesta Correcta")
            nota=nota+50
        else:
            print("Respuesta incorrecta")
        
        print("Nota Final")
        print("La nota final del Examen del estudiante", self.nombre, "es ",nota )
    def estudiar(self):
        print(self.nombre, " esta estudiando para su examen ")

#Paso 3 - DEFINIR LOS OBJETOS
#docente, 22 estudiantes
docente=ProgramacionI("Kevin Arroyo Montaño","Sistemas Informaticos",27,45451,"a@gmail.com")           
estudiante1=ProgramacionI("Felix Paye","Sistemas Informaticos",27,45451,"a@gmail.com")
estudiante2=ProgramacionI("Ismael","Sistemas Informaticos",27,45451,"a@gmail.com")
estudiante3=ProgramacionI("Heber","Sistemas Informaticos",27,45451,"a@gmail.com")
estudiante4=ProgramacionI("Ernesto","Sistemas Informaticos",27,45451,"a@gmail.com")
estudiante5=ProgramacionI("Praxides","Sistemas Informaticos",27,45451,"a@gmail.com")
estudiante6=ProgramacionI("Wilder","Sistemas Informaticos",27,45451,"a@gmail.com")
estudiante7=ProgramacionI("Cesar","Sistemas Informaticos",27,45451,"a@gmail.com")

estudiante1.estudiar()
estudiante5.estudiar()
estudiante7.estudiar()

estudiante5.darExamen()

parcial1=int(input("Ingrese la nota del primer parcial: "))
parcial2=int(input("Ingrese la nota del segundo parcial: "))
final=int(input("Ingrese la nota del examen final: "))
docente.calificar(parcial1,parcial2,final)