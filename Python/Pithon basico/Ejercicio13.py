# Ejercicio 13. Función sumar_listas usando lambdas
# Descripción: Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista_numeros_1 = [1, 4, 5, 6, 7, 7]
lista_numeros_2 = [3, 11, 34, 56]
sumar_listas = list(map(lambda x, y: x + y, lista_numeros_1[:len(lista_numeros_2)], lista_numeros_2))