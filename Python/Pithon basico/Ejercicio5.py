# Ejercicio 5. Función es_anagrama
# Descripción: Crea una función que determine si dos palabras son anagramas.
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())