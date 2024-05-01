

#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona
#Introduce el peso en kg
Peso = 80
#Introduce la altura en m
Altura = 1.7

def IMC (P,A):
  Resultado=P/(A*A)
  print(f"El IMC es {Resultado}")

IMC(Peso, Altura)