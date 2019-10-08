"""
    Dada la siguiente estructura de datos

    [(10,2), (8,7), (5,4), (3,11), (10,11)]
"""
import math
datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]

raiz = lambda x: x[0] # Posición para sacar raices 10,8,5,3,10
pot = lambda x: x[1] # Posición para sacar potencias 2,7,4,11,11

funcion = lambda x: (math.sqrt(raiz(x)), (pot(x) **2)) # Creacion de una lista con tuplas de raiz y potencia

print(list(map(funcion, datos)))
