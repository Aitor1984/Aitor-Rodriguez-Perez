

#Escribe un programa que determine si un número ingresado por el usuario es primo o no.


#Introduce un número
Numero=[43, 54, 71, 88, 67]
#Vamos a dividir estos numeros entre los primeros números primos hasta que el cociente sea entero (no primo) o menor que el divisor (primo)

def test_primo(N):
  Primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 , 97]
  for P in Primos:
      if N/P < P and N/P != int(N/P):
         print(f"El número {N} es un número primo")
         break
      if N/P == int(N/P):
         print(f"El número {N} no es un número primo")
         break
      if P==97 and N/P > P:
         print(f"Lo siento, no he podido hacer la comprobación")
         break
      

for N in Numero:
   test_primo(N)
  
