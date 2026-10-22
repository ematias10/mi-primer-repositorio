def dividir(a, b):
    try:
        resultado = a/b
        print(f"El resultado de {a}/{b} = {resultado}")
    except ZeroDivisionError:
        print(f"ERROR: No se puede dividir por 0.")
    except TypeError:
        print(f"ERROR: Uno de los valores proporcionados no es un número.")
    except Exception as e:
        print(f"ERROR: {e}")
    except err
    
dividir(9,0)
dividir("a",3)
dividir(36,8)
dividir(40,5)
dividir(10,67)
dividir(0,9)


