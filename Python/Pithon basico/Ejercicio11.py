# Ejercicio 11. Función numeros_pares usando lambdas y filter
# Descripción: Crea una función lambda que filtre los números pares de una lista dada.
lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_pares = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lista_numeros))