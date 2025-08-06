from dataclasses import dataclass, field
@dataclass()
class Mesa:
    numero: int
    pedidos: list[dict] = field(default_factory=list)
    total: float = 0.0