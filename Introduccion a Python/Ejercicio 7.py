#Escoge dos números
N1 = 3
N2 = 4
#Escoge operación: Suma, Resta, Multiplicación o División
Operación = ["suma", "resta","multiplicacion","division"]
Resultado = 0

def calculadora(Numero1, Numero2, Operando):
   if Operando == "suma":
      print(f"Operación: {Operando}")
      print(f"Número 1: {Numero1}")
      print(f"Número 1: {Numero2}")
      print(f"El resultado de la operación és {Numero1+Numero2}")
   if Operando == "resta":
      print(f"Operación: {Operando}")
      print(f"Número 1: {Numero1}")
      print(f"Número 1: {Numero2}")
      print(f"El resultado de la operación és {Numero1-Numero2}")
   if Operando == "multiplicacion":
      print(f"Operación: {Operando}")
      print(f"Número 1: {Numero1}")
      print(f"Número 1: {Numero2}")
      print(f"El resultado de la operación és {Numero1*Numero2}")  
   if Operando == "division":
      print(f"Operación: {Operando}")
      print(f"Número 1: {Numero1}")
      print(f"Número 1: {Numero2}")
      print(f"El resultado de la operación és {Numero1/Numero2}")

for ops in Operación:
    calculadora(N1,N2,ops)