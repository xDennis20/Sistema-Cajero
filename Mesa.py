from dataclasses import dataclass, field
@dataclass()
class Mesa:
    numero: int
    pedidos: list[dict] = field(default_factory=list)
    total: float = 0.0
    
    def agregar_pedido(self, nombre: str, precio: float):
        self.pedidos.append({"Comida": nombre,"Precio": precio})
        self.total += precio