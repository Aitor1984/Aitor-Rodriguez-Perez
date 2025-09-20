

#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta
Precios = [12, 24, 3, 51, 35]
Total=0
def Due_tip(lista):
     Carrito = 0
     for precio in lista:
         Carrito = precio*1.15 + Carrito
     return Carrito       

Total= Due_tip(Precios)
print(f"El total a pagar es {Total}€, incluyendo {Total*0.15}€ de propina")