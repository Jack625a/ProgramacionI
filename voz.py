#17/08/2023
#Librerias Externas
#Reconocimiento de voz
#Paso 1.  Instalar las Dependencias
#pyttsx3 = Nos sirve para convertir texto a voz
#speech_recognition= Para reconocer la voz y convertirlo a texto
#1. pip install SpeechRecognition
#2. pip install Pyaudio
#3. Probar= python -m speech_recognition
#Codigo para mostrar la lista de Microfonos
#Paso 2. Seleccionar el microfono a utilizar= index=2
#Paso 3. Instalar el conversor de texto a voz
# pip install pyttsx3

#Ejercicio 1. Reconocimiento de Voz - Conversión de texto a Voz

#Paso 4. Importar las bibliotecas
import pyttsx3
import speech_recognition as sr 

#Paso 5. CREAR LA FUNCION PRINCIPAL RECONOCIMIENTO DE VOZ
def reconocer():
    #InicialiZamos el Reconocimiento de Voz
    r=sr.Recognizer()
    #Definir la voz que se utiliZARa
    engine=pyttsx3.init()
    voices_id="spanish-mexican"
    engine.setProperty('voice',voices_id)

    #Pedir al usuario que hable y esperar que se detecte la voz
    engine.say("Que opcion desea realiZAr?")
    engine.runAndWait()

    with sr.Microphone(device_index=2) as source:
        audio=r.listen(source)

    #Procesar la voz y dar el resultado
    try:
        texto=r.recognize_google(audio,language="es-MX")
        print("Usted dijo: ",texto)
    except sr.UnknownValueError:
        engine.say("No se ha podido entender lo que dijo, por favor intene nuevamente")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say("Ha ocurrido un error al intentar reconocer la voz error: ",e)
        engine.runAndWait()

#Paso 6- Crear la funcion principal
def menu():
    #Inicializar el conversor
    engine=pyttsx3.init()
    voices_id="spanish-mexican"
    engine.setProperty('voice',voices_id)

    #Mostrar un menu de opciones
    while True:
        engine.say("Seleccione una opcion: ")
        engine.say("1. Opcion1")
        engine.say("2. Opcion2")
        engine.say("3. Opcion3")
        engine.say("4. Opcion4")
        engine.runAndWait()

        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            reconocer()
        elif opcion=="2":
            engine.say("Se selecciono la opcion 2")
            engine.runAndWait()
            break
        elif opcion=="3":
            engine.say("Se selecciono la opcion 3")
            engine.runAndWait()
        elif opcion=="4":
            engine.say("Se selecciono la opcion 4")
            engine.runAndWait()
        else:
            engine.say("Opcion invalida")
            engine.runAndWait()

menu()