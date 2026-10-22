import json
import time

from consulta_prompt import armar_peticion, enviar_peticion, extraer_texto
from limpiador_respuestas_json import parsear_respuesta_json

BANCO_DE_PROMPTS = [
	{
    	"nombre": "clasificar_sentimiento",
    	"system_instruction": (
        	"Responde únicamente con un JSON con las claves 'sentimiento' "
        	"('positivo', 'negativo' o 'neutro') y 'confianza' (0 a 1)."
    	),
    	"ejemplo_usuario": "El servicio llegó tarde pero el producto está perfecto.",
    	"claves_esperadas": ["sentimiento", "confianza"],
    	"response_schema": {
        	"type": "OBJECT",
        	"properties": {
            	"sentimiento": { "type": "STRING" },
            	"confianza": { "type": "NUMBER" }
        	},
        	"required": ["sentimiento", "confianza"]
    	},
	},
    {
        "nombre": "clasificar_categoria",
        "system_instruction": (
            "Responde únicamente con un JSON con las claves 'categoria' "
            "('soporte', 'ventas' o 'otros') y 'confianza' (0 a 1)."
        ),
        "ejemplo_usuario": "Necesito ayuda para resetear mi contraseña.",
        "claves_esperadas": ["categoria", "confianza"],
        "response_schema": {
            "type": "OBJECT",
            "properties": {
                "categoria": { "type": "STRING" },
                "confianza": { "type": "NUMBER" }
            },
            "required": ["categoria", "confianza"]
        }
    },
    {
        "nombre": "clasificar_urgencia",
        "system_instruction": (
            "Responde únicamente con un JSON con las claves 'urgencia' "
            "('alta', 'media' o 'baja') y 'confianza' (0 a 1)."
        ),
        "ejemplo_usuario": "Necesito que mi problema se resuelva lo antes posible.",
        "claves_esperadas": ["urgencia", "confianza"],
        "response_schema": {
            "type": "OBJECT",
            "properties": {
                "urgencia": { "type": "STRING" },
                "confianza": { "type": "NUMBER" }
            },
            "required": ["urgencia", "confianza"]
        }
    }
]

if __name__ == '__main__':
	registro = {}
	
	for prompt in BANCO_DE_PROMPTS:
		exitos = 0
		intentos = 3
		for intento in range(intentos):
			url, body = armar_peticion(
				prompt["ejemplo_usuario"],
				prompt["system_instruction"],
				prompt.get("response_schema"),
			)
			respuesta = enviar_peticion(url, body)
			texto = extraer_texto(respuesta)
			print(f"Respuesta recibida: {texto}")
			try:
				datos = parsear_respuesta_json(texto)
				print(f"Datos parseados: {datos}")
				if all(clave in datos for clave in prompt["claves_esperadas"]):
					exitos += 1
			except ValueError as error:
				print(f"  intento {intento + 1} falló: {error}")
			time.sleep(1)
		print(f"{prompt['nombre']}: {exitos}/{intentos} respuestas válidas")
		registro[prompt["nombre"]] = {"exitos": exitos, "intentos": intentos}

	
		with open("prompts/registro_resultados.json", "w", encoding="utf-8") as archivo:
			json.dump(registro, archivo, indent=2, ensure_ascii=False)