

#Crea un programa que sume todos los números en una lista ingresada por el usuario.
#Introduce una lista de números:
Lista= [4,54,765,43,67,87]

def suma(N):
  Total=0
  for Q in N:
    Total=Total+Q
  print(f"La suma total es {Total}")

suma(Lista)