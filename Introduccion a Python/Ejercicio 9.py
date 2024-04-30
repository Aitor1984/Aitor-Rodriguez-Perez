#Introduce la cantidad en dolares
Dolar = [80,45,65,321,5554] 

def conversor (D):
  Resultado=D*0.85
  print(f"{D} dolares son {Resultado} euros")

for Q in Dolar:
  conversor(Q)