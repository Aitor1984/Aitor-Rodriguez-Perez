

#Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

#Introduce un número entre 1 y 7
Dia = [1,2,3,4, 56,5,6, -9,7] 

def semana (D):
  if D == 1:
     print(f"Has escogido el Lunes")
  if D == 2:
     print(f"Has escogido el Martes")
  if D == 3:
     print(f"Has escogido el Miercoles")
  if D == 4:
     print(f"Has escogido el Jueves")
  if D == 5:
     print(f"Has escogido el Viernes")
  if D == 6:
     print(f"Has escogido el Sábado")   
  if D == 7:
     print(f"Has escogido el Domingo") 
  if D > 7 or D<0:
     print(f"Por favor, escoge un número entre el 1 y el 7")    

for D in Dia:
  semana(D)