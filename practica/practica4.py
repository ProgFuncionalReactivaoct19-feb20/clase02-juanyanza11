"""
    Dada la siguiente estructura de datos

[10,2,8,7,5,4,3,11,0, 1]

Use:
Función map
Una función anónima
que permita presentar en otra lista, cada elemento elevado a la tercera potencia.
"""
datos = [10,2,8,7,5,4,3,11,0,1]
funcion = lambda x: x**3 # Funcion lambda para elevar cada elementode la lista al cuadrado
print(list(map(funcion, datos)))
