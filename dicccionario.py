diccionario = {
   "texto": "Hola, soy una respuesta generada",
   "detalles": {
     "modelo": "gemini-flash-2.5",
     "tokens": 12,
     "mas_detalles": {
         'id_consulta': 283128,
         'tokens_totales': 378,
         'tiempo_rpta': 0.2,
     }
   }
}

#KEY: VALUE o LLAVE: VALOR
print(diccionario["texto"])
dict_de_detalles = diccionario["detalles"]
print(dict_de_detalles["modelo"])