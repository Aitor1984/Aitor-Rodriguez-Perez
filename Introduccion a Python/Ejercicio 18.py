#Introduce una oración
Oracion1="El patio de mi casa es particular"
Oracion2="Hola"
Oracion3="Hoy es martes"

def contador_p(O):
  Palabras=1
  for P in O:
    if P == " ":
       Palabras +=1
  print(f"La frase ({O}) tiene {Palabras} palabras en total")
contador_p(Oracion1)
contador_p(Oracion2)
contador_p(Oracion3)