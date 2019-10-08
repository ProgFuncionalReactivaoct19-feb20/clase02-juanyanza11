"""
    Desarrollar una función anónima que permita retornar la siguiente salida,
    ejemplo:
    CUENCA capital de AZUAY
"""
# Funcion lambda para concatenar cadenas
cadena_personalizada = lambda cadena, cadena2: "%s capital de %s" % \
(cadena.upper(),cadena2.upper())
# Función upper para ponner convertir en mayuscylas

print(cadena_personalizada("Cuenca", "Azuay"))
