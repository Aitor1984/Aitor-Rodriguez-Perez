

#Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

Suma_pares=0
n = 0
while n <=100:
  n+=1
  if n % 2 ==0:
      Suma_pares = Suma_pares + n

print(f"La suma de todos los numeros pares del 1 al 100 es {Suma_pares}")

