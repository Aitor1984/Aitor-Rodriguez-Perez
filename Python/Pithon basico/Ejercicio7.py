# Ejercicio 7. Función fibonacci
# Descripción: Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)