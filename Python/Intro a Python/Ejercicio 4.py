

#Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario
Palabra = "Fulanito"
Vocales = "AEIOUaeiou"
def Contador_vocales(palabra):
  Cuenta=0
  for letra in palabra:
    for vocal in Vocales:
      if letra == vocal:
        Cuenta = Cuenta +1
        break
  return Cuenta                
print(f"La palabra {Palabra} tiene {Contador_vocales(Palabra)} vocales")

