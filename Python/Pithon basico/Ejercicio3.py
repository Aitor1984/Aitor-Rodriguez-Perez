# Ejercicio 3. Función encontrar_duplicado
# Descripción: Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def encontrar_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None