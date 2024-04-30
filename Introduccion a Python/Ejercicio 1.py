Termometro = [12, 12, 45, 54, 32, -12]
def conversor(temperatura):
  for datos in temperatura:
    resultado = (datos * 9/5)+32
    print (f"{datos} grados Celsius son {resultado} grados Farenheit") 

conversor (Termometro)