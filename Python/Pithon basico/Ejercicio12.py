# Ejercicio 12. Función numeros_suma usando lambdas y map
# Descripción: Crea una función lambda que sume 3 a cada número de una lista dada.
lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_suma = list(map(lambda x: x + 3, lista_numeros))
print("Resultado de sumar 3 a cada número:", numeros_suma)