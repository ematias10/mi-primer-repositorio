import json
import re

def parsear_respuesta_json(texto):
	print(f"Texto recibido para parsear: {texto}")
	texto_limpio = texto.strip()
	texto_limpio = re.sub(r"^```(?:json)?\s*", "", texto_limpio)
	texto_limpio = re.sub(r"\s*```$", "", texto_limpio)
	try:
		datos = json.loads(texto_limpio)
	except json.JSONDecodeError:
		raise ValueError("La respuesta del modelo no es JSON válido.")
	except Exception as e:
		raise ValueError(f"Error al parsear JSON: {e}")
	finally:
		print(f"completado parseo de JSON")
	return datos