"""
        Ejemplo 3: uso de funcion lambda
"""
datos = ((30, 1.79),(25, 1.60),(35, 1.68)) #Tupla que contiene otra tupla de dos elementos
dato = lambda x: x[2]

print(dato(datos))
