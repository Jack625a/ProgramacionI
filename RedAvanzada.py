#Ejercicio 2- 24-08-2023
#Crear un asistente virtual con redes neuronales
#Paso 1. Importar las librerias
import openai
import pyttsx3
import speech_recognition as sr 
openai.api_key=""
#Funciones para opcion 
#1. Funcion para generar Texto
def obtenerRespuesta(pregunta):
    respuesta=openai.Completion.create(
        prompt=pregunta,
        engine="text-davinci-003",
        temperature=0.5, #0-1
        max_tokens=350
    )
    return respuesta.choices[0].text.strip()
    

#CFuncion para la Voz
def reconocer():

    #InicialiZamos el Reconocimiento de Voz
    r=sr.Recognizer()
    #Definir la voz que se utiliZARa
    engine=pyttsx3.init()
    voices_id="spanish-mexican"
    engine.setProperty('voice',voices_id)

    #Pedir al usuario que hable y esperar que se detecte la voz
    engine.say("Hola bienvenido cual es tu consulta?")
    engine.runAndWait()

    with sr.Microphone(device_index=2) as source:
        audio=r.listen(source)

    #Procesar la voz y dar el resultado
    try:
        pregunta=r.recognize_google(audio,language="es-MX")
    except sr.UnknownValueError:
        print("No se ha podido entender lo que dijo, por favor intene nuevamente")
        #engine.runAndWait()
    except sr.RequestError as e:
        print("Ha ocurrido un error al intentar reconocer la voz error: ",e)
        #engine.runAndWait()


#Funcion para el menu principal
def menu():
    while True:
        print("===ASISTENTE VIRTUAL===")
        print("1. Chatbot")
        print("2. ChatBot mediante voz")
        print("3. Asistente Virtual")
        print("4. Selector de Musica")
        print("5. Salir")
        opcion=int(input("Ingrese una opción: "))
        if opcion==1:
            #Opcion1 CHATBOT
            while True:
                opcion=int(input("Desea seguir utilizando el servicio? 1. para Continuar, 2. No para Salir"))
                if opcion==1:
                    pregunta=input("Hola, cual es tu consulta? ")
                    respuesta=obtenerRespuesta(pregunta)
                    print(respuesta)
                elif opcion==2:
                    print("Gracias por utilizar el servicio de Inteligencia Artificial")
                    break
                else:
                    print("Error, operación invalida")
            
        elif opcion==2:
            while True:
                opcion=int(input("Desea seguir utilizando el servicio? 1. para Continuar, 2. No para Salir"))
                if opcion==1:
                    print("Cual es su consulta?")
                    #InicialiZamos el Reconocimiento de Voz
                    r=sr.Recognizer()
                    #Definir la voz que se utiliZARa
                    engine=pyttsx3.init()
                    voices_id="spanish-mexican"
                    engine.setProperty('voice',voices_id)

                    #Pedir al usuario que hable y esperar que se detecte la voz
                    engine.say("Hola bienvenido cual es tu consulta?")
                    engine.runAndWait()

                    with sr.Microphone(device_index=2) as source:
                        audio=r.listen(source)

                    #Procesar la voz y dar el resultado
                    try:
                        pregunta=r.recognize_google(audio,language="es-MX")
                        respuesta=obtenerRespuesta(pregunta)
                        print(respuesta)
                    except sr.UnknownValueError:
                        print("No se ha podido entender lo que dijo, por favor intene nuevamente")
                        #engine.runAndWait()
                    except sr.RequestError as e:
                        print("Ha ocurrido un error al intentar reconocer la voz error: ",e)
                        #engine.runAndWait()
                elif opcion==2:
                    break
                else:
                    print("Operacion no valida")
            #Opcion2 CHATBOT VOZ
            
        elif opcion==3:
            asistente()
            #Opcion3 ASISTENTE VIRTUAL
            print("#Opcion3 ASISTENTE VIRTUAL")
        elif opcion==4:
            print("#Opcion4 MUSICA")
            musica()
            #Opcion4 MUSICA
        elif opcion==5:
            break
        else:
            print("Operacion no valida")

menu()