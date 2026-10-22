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

##### COMO FUNCIONA UN DICCIONARIO
dict = {
    "clave1": "valor1",
    "clave2": "valor2"
}

# Accedemos a un valor usando su clave
print(dict["clave1"])

# Podemos agregar un nuevo par clave-valor
dict["clave3"] = "valor3"
print(dict["clave3"])

# Podemos eliminar un par clave-valor
del dict["clave2"]
print(dict)

# Podemos verificar si una clave existe en el diccionario
print("clave1" in dict)
print("clave2" in dict)

# Podemos obtener todas las claves y valores del diccionario
print(dict.keys())
print(dict.values())

# Podemos obtener todos los pares clave-valor como tuplas
print(dict.items())

# Podemos obtener el valor de una clave de manera segura usando get()
print(dict.get("clave1"))
print(dict.get("clave2"))
print(dict.get("clave4", "No existe"))

# Podemos actualizar el valor de una clave existente
dict["clave1"] = "nuevo_valor1"
print(dict["clave1"])

# Podemos actualizar varios valores a la vez usando update()
dict.update({
    "clave1": "valor_actualizado1",
    "clave3": "valor_actualizado3"
})
print(dict)

# Podemos eliminar todos los elementos del diccionario usando clear()
dict.clear()
print(dict)

# Podemos crear un diccionario a partir de una lista de tuplas
lista_de_tuplas = [("clave1", "valor1"), ("clave2", "valor2")]

dict_desde_tuplas = dict(lista_de_tuplas)
print(dict_desde_tuplas)

# Podemos clonar un diccionario usando copy()
dict_clonado = dict_desde_tuplas.copy()
print(dict_clonado)
# copia profunda usando copy()
import copy
dict_clonado_profundo = copy.deepcopy(dict_desde_tuplas)
print(dict_clonado_profundo)

# Podemos eliminar un elemento y obtener su valor usando pop()
valor_eliminado = dict_clonado.pop("clave1", "No existe")
print(valor_eliminado)
print(dict_clonado)