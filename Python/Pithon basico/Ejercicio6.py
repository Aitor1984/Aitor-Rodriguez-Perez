# Ejercicio 6. Función buscar_nombre
# Descripción: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
def buscar_nombre():
    nombres = ["Jaime", "Silvia", "Ana"]
    nombre_buscar = input("Introduce el nombre a buscar: ")
    if nombre_buscar in nombres:
        print(f"{nombre_buscar} fue encontrado en la lista.")
    else:
        raise ValueError(f"{nombre_buscar} no está en la lista.")