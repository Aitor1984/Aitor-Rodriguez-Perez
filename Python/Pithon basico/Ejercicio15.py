# Ejercicio 15. Clase UsuarioBanco
# Descripción: Representa a un usuario de un banco con métodos para operar con su saldo.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario origen no tiene suficiente saldo.")
        otro_usuario.retirar_dinero(cantidad)
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad