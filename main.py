import os
from dotenv import load_dotenv
#Importar función desde archivo que no está en la raíz
from functions.function_suma import suma

load_dotenv()


if __name__ == '__main__':

    api_key = os.getenv("API_KEY")
    usuario = os.getenv("USUARIO")

    print(f"Hola {usuario}, se tu key, es: {api_key}")
    print(f"El resultado de la suma es de: {suma(10,9)}")

