#Ejercicio 1 - 10/08/2023
#Conexion con Apis (RED NEURONAL - OPENAI)
import openai
openai.api_key=""

def obtenerRespuesta(pregunta):
    respuesta=openai.Completion.create(
        prompt=pregunta,
        engine="text-davinci-003",
        temperature=0.5, #0-1
        max_tokens=350
    )
    return respuesta.choices[0].text.strip()
#Funcion principal
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