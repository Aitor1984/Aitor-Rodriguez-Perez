

#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.


#Introduce el número de minutos
Minutos = [158, 445, 9856, 33578]

def conversor(M):
  Horas=int(M/60)
  Minutos_restantes=M-Horas*60
  print(f"{M} minutos serían {Horas} horas y {Minutos_restantes} minutos")

for Q in Minutos:
  conversor(Q)