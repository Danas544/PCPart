from typing import Optional


class PCPart:
    def __init__(self, name: str, price: float, color: Optional[str] = None):
        self.name = name
        self.price = price
        self.color = color

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_color(self) -> Optional[str]:
        return self.color


class CPU(PCPart):
    def __init__(
        self,
        name: str,
        price: float,
        brand: str,
        speed: str,
        power_usage: str,
        color: Optional[str] = None,
    ):
        super().__init__(name, price, color)
        self.brand = brand
        self.speed = speed
        self.power_usage = power_usage

    def get_brand(self) -> str:
        return self.brand

    def get_speed(self) -> str:
        return self.speed

    def get_power_usage(self) -> str:
        return self.power_usage


class GPU(PCPart):
    def __init__(
        self,
        name: str,
        price: float,
        brand: str,
        memory: str,
        color: Optional[str] = None,
    ):
        super().__init__(name, price, color)
        self.brand = brand
        self.memory = memory

    def get_brand(self) -> str:
        return self.brand

    def get_memory(self) -> str:
        return self.memory
