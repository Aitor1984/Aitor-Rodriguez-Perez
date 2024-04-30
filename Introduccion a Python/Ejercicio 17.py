#Introduce la distancia en millas
Millas = [80,45,65,321,5554] 

def conversor (M):
  Resultado=M*1.60934
  print(f"{M} millas son {Resultado} km")

for Q in Millas:
  conversor(Q)