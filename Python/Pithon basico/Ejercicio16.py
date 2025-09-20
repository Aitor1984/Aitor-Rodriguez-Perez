# Ejercicio 16. Función procesar_texto
# Descripción: Procesa un texto según la opción especificada: contar, reemplazar, eliminar.
def contar_palabras(texto):
    palabras = texto.lower().replace('.', '').split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    return ' '.join([p for p in texto.split() if p != palabra])

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida.")

# Caso de uso para procesar_texto
texto_ejemplo = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
print(procesar_texto(texto_ejemplo, "contar"))
print(procesar_texto(texto_ejemplo, "reemplazar", "texto", "relato"))
print(procesar_texto(texto_ejemplo, "eliminar", "ejemplo"))