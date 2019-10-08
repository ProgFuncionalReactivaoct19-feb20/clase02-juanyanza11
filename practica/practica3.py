"""
    Dada la siguiente llamada a una función anónima:

    suma(10,11)

    Desarrollar la función; debe presentar en pantalla para el ejemplo 21
"""
datos = (10,11)

sumar = lambda x: x[0] + x[1] # elemento de la Posición 1 mas el elemento de la Posición 2
print(sumar(datos))
