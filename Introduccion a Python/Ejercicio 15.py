#Introduce el número de minutos
Minutos = [158, 445, 9856, 33578]

def conversor(M):
  Horas=int(M/60)
  Minutos_restantes=M-Horas*60
  print(f"{M} minutos serían {Horas} horas y {Minutos_restantes} minutos")

for Q in Minutos:
  conversor(Q)