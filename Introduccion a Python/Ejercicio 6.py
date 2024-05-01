

#Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

Palabra1 = "Reconocer"
Palabra2 = "Fulanito"

def Busca_palindromo(palabras):
  palabra=palabras.lower()
  L=len(palabra)
  Pos1 = 0
  Pos2 = L-1
  while Pos1!=Pos2:
        if palabra[Pos1] == palabra[Pos2]:
           Pos1+=1
           Pos2-=1
        else: 
           print(f"La palabra {palabra} no es un palíndromo")
           break
  if Pos1==Pos2:  
    print(f"La palabra {palabra} es un palíndromo")
   

Busca_palindromo(Palabra1)
Busca_palindromo(Palabra2)


