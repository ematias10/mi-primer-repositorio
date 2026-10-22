import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()
    
def armar_peticion(pregunta):
     api_key = os.getenv("GEMINI_API_KEY")
     modelo = "gemini-3.5-flash-lite"
     url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
     body = {
            "contents": [
                {"parts": [{"text": pregunta}]}
            ]
     }
     return url, body

def enviar_peticion(url, body):
     respuesta = requests.post(url, json=body)
     datos = respuesta.json()
     return datos

def extraer_texto(datos):
     return datos["candidates"][0]["content"]["parts"][0]["text"]

def obtener_datos_prueba(pregunta):
     url, body = armar_peticion(pregunta)
     datos = enviar_peticion(url, body)
     return extraer_texto(datos)

if __name__ == '__main__':
     respuesta_gemini = obtener_datos_prueba('hola gemini, como estas?')
     print(f"La respuesta de Gemini es: {respuesta_gemini}")
     pregunta = 'Hola gemini, como estas?'
     
     latencias = []
     for i in range(10):
          url, body = armar_peticion(pregunta)
          inicio = time.perf_counter() # <--- Inicia el conteo de tiempo
          respuesta_json = enviar_peticion(url, body)
          fin = time.perf_counter() # <--- Termina el conteo de tiempo
          latencias.append(fin - inicio)
          print(f"Intento {i + 1}: {latencias[-1]:.2f} segundos")
     
     latencia_promedio = sum(latencias) / len(latencias)
     print(f"Latencia promedio: {latencia_promedio:.2f} segundos")