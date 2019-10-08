"""
    Ejercicio 1: Desarrollar la función anónima que retorne True or False si
    el número dado es par.
    author: juanyanza11
"""
valor_par = (lambda num: num % 2 == 0) # validacion si es par con cociente cero

print(valor_par(2))
print(valor_par(3))
print(valor_par(11))
