import os
import requests
from dotenv import load_dotenv
import time
# Importa la función para limpiar y parsear respuestas JSON del modelo Gemini
from limpiador_respuestas_json import parsear_respuesta_json

load_dotenv()



"""
Arma la petición para el modelo Gemini.
Recibe la pregunta del usuario, la instrucción del sistema y opcionalmente un esquema de respuesta.
Devuelve la URL y el cuerpo de la petición.
si no se proporciona un esquema de respuesta, se omite en la petición. (None por defecto)
"""
def armar_peticion(pregunta_usuario, system_instruction, response_schema=None):
     api_key = os.getenv("GEMINI_API_KEY")
     modelo = "gemini-3.5-flash-lite"
     url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
     # Arma el cuerpo de la petición con la instrucción del sistema y la pregunta del usuario
     body =  {
          "systemInstruction": {
               "parts": [ { "text": system_instruction } ]
          },
          "contents": [
               { "parts": [ { "text": pregunta_usuario } ] }
          ]
     }

     # Si se proporciona un esquema de respuesta, se agrega a la configuración de generación
     if response_schema is not None:
          # Agrega la configuración de generación con el esquema de respuesta
          body["generationConfig"] = {
               "responseMimeType": "application/json",
               "responseSchema": response_schema
          }

     return url, body

def enviar_peticion(url, body):
     respuesta = requests.post(url, json=body)
     datos = respuesta.json()
     return datos

def extraer_texto(datos):
     return datos["candidates"][0]["content"]["parts"][0]["text"]

def obtener_datos_prueba(pregunta):
     system_instruction = "Eres un asistente técnico. Responde siempre en un máximo de 3 oraciones."
     url, body = armar_peticion(pregunta, system_instruction)
     datos = enviar_peticion(url, body)
     return extraer_texto(datos)

if __name__ == '__main__':
     # Esquema de respuesta esperado del modelo Gemini
     response_schema = {
          "type": "OBJECT", # El tipo de la respuesta esperada es un objeto JSON
          "properties": { # Las propiedades esperadas en la respuesta JSON
               "categoria": { "type": "STRING" }, # La categoría de la respuesta y la respuesta proporcionada por el modelo como cadena de texto
               "confianza": { "type": "NUMBER" } # El nivel de confianza del modelo en la categoría y la respuesta proporcionada como número
          },
          "required": ["categoria", "confianza"] # Las propiedades que son obligatorias en la respuesta JSON
     }
     # Pregunta del usuario que se enviará al modelo Gemini (Contenido de la pregunta, tarea o consulta específica)
     pregunta_usuario = "Necesito ayuda para resetear mi contraseña, no me llega el correo de verificación."
     # Instrucción del sistema que se enviará al modelo Gemini (Rol y Formato de respuesta esperado)
     system_instruction = (
	     "Responde únicamente con un objeto JSON válido, sin texto adicional "
	     "y sin usar bloques de markdown. El JSON debe tener exactamente estas "
	     "claves: 'categoria' (string) y 'confianza' (número entre 0 y 1)."
     )

     url, body = armar_peticion(pregunta_usuario, system_instruction, response_schema)
     respuesta_json = enviar_peticion(url, body)
     texto = extraer_texto(respuesta_json)
     datos = parsear_respuesta_json(texto)
     
     print(datos)
     print(type(datos))
     