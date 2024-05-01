

#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

#Introduce tu año de nacimiento
Año=[1984, 2005, 1962]
#Año actual
from datetime import date
today = date.today()

def Edad(N):
  print(f" Este año {today.year} cumpliras {today.year-N} años")

for Q in Año:
  Edad(Q)