from typing import Dict
from Mesa import Mesa
class Cajero:
    def __init__(self):
        self.mesas: Dict[int, Mesa] = {}
    
    def crear_mesa(self, numero: int):
        if numero in self.mesas:
            print(f"La Mesa {numero} ya existente")
            return
    
        self.mesas[numero] = Mesa(numero)
        print(f"Mesa {numero} fue creada con exito")
    
    def registrar_pedido_en_mesa(self,numero_mesa: int):
        if numero_mesa in self.mesas:
            comida = input("Ingrese el nombre de la comida o bebida: ")
            precio = int(input("Ingrese el precio de la comida o bebida: "))
            self.mesas[numero_mesa].agregar_pedido(comida,precio)
            print(f"El pedido fue registrado correctamente en la mesa {numero_mesa}")
        else:
            print("La mesa que intento registrar el pedido no existe.")
