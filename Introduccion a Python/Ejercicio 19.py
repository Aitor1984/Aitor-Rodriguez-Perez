

#Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no

#Introduce un año
Año=[1984, 1962, 2019, 1988, 1900, 2025, 2028]

def bisiesto(A):
    Cuenta=0
    Cuenta=2024-A
    if Cuenta %4 ==0:
        print(f"El año {A} es bisiesto")
    if Cuenta %4 !=0:
        print(f"El año {A} no es bisiesto")

for Q in Año:
    bisiesto(Q)