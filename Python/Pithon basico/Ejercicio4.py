# Ejercicio 4. Función enmascarado_datos
# Descripción: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarado_datos(valor):
    texto = str(valor)
    return '#' * (len(texto) - 4) + texto[-4:]