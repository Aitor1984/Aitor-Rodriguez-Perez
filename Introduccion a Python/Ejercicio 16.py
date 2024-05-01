

#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

#Introduce una lista de numeros
Lista = [2,53,15,12,36,28,45,69]

def splitter(N):
  Pares=[]
  Impares=[]
  Contador_P=0
  Contador_I=0
  for L in N:
    if L%2 == 0:
         Contador_P += 1
         Pares.append(L)
    if L%2 != 0:
         Contador_I += 1
         Impares.append(L)
  print(f"Hay {Contador_I} números impares y son {Impares}")
  print(f"Hay {Contador_P} números impares y son {Pares}")

splitter(Lista)
