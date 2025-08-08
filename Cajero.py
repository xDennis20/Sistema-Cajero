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
    
    def registrar_pedido_en_mesa(self,numero_mesa: int, comida: str, precio: float):
        if numero_mesa in self.mesas:
            self.mesas[numero_mesa].agregar_pedido(comida,precio)
            print(f"El pedido fue registrado correctamente en la mesa {numero_mesa}")
        else:
            print("La mesa que intento registrar el pedido no existe.")

    def cobrar_mesa(self,numero_mesa: int,dinero_cliente: float):
        if numero_mesa in self.mesas:
            mesa = self.mesas[numero_mesa]
            if dinero_cliente < mesa.total:
                print(f"Falta ${(mesa.total - dinero_cliente):.2f} para poder cubrir el total.")
                return
            vuelto = dinero_cliente - mesa.total
            print(f"Vuelto a dar al cliente es: {vuelto:.2f}")
        else:
            print("La mesa que ingreso no existe")

    def resumen_dia(self):
        print("*** RESUMEN DEL DIA ***")
        for key,valor in self.mesas.items():
            print(f"La Mesa {key} genero un total de ${valor.total:.2f}")