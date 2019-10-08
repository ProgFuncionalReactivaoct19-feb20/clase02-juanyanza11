"""
  Ejemplo 6: usando funciones lambda
"""
lista = [10,2,3,5,1]

funciones = lambda x: x + 100
print(min(list(map(funciones, lista))))
