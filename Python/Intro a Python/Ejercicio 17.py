

#Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.


#Introduce la distancia en millas
Millas = [80,45,65,321,5554] 

def conversor (M):
  Resultado=M*1.60934
  print(f"{M} millas son {Resultado} km")

for Q in Millas:
  conversor(Q)