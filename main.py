# Phase 1:
# Create a class that would represent pc parts. It should contain basic methods to retreive items name, price, colour (if applicable).
# PC part list can be found here: https://pcpartpicker.com/list/
# The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
# At this stage, dictionary data structures can work as Database. OOP abstraction, inheritance and encapsulation must be presented in a code base.
# Unit tests must be written for the methods.

# Phase 2:
# Add logging to all necessary functionality to see the data flow (with logger config.).
# Add exception handling , describe your own exceptions if necessary.
# Create functions that would update current datasets (database).
# Add functions that would parse durrent datasets(database) by specific parameters (CPU name = 'AMD')
# Use  List, Dict comprehentions to get parsed data.
import logging
import logging.config
from typing import Optional, List, Union
from error_exception import PartNotFoundError, DuplicatePartError

logging.config.fileConfig("logging_config.ini", disable_existing_loggers=False)

logger = logging.getLogger(__name__)


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


class PCPartDatabase:
    def __init__(self):
        self.parts = {}

    def add_part(self, part: Union[CPU, GPU]) -> None:
        part_name = part.get_name()
        if part_name in self.parts:
            logger.warning(f"Part '{part_name}' already exists in the database.")
            raise DuplicatePartError(f"Part '{part_name}' already exists in the database.")
        self.parts[part_name] = part
        logger.info(f"Added {part_name} to the database.")

    def get_part(self, name: str) -> Optional[Union[CPU, GPU]]:
        try:
            part = self.parts[name]
        except KeyError:
            logger.warning(f"{name} not found in the database.")
            raise PartNotFoundError(f"Part '{name}' not found in the database.")
        return part
    

    def get_all_parts(self) -> List[Union[CPU, GPU]]:
        return list(self.parts.values())

    def update_part_price(self, name: str, new_price: float) -> None:
        part = self.get_part(name)
        if part:
            part.price = new_price
            logger.info(f"Updated the price of {name} to {new_price}.")


if __name__ == "__main__":
    database = PCPartDatabase()

    cpu1 = CPU("Intel i7", 300, "Intel", "3.5 GHz", "95W")
    cpu2 = CPU("AMD Ryzen 5", 250, "AMD", "3.8 GHz", "85W")
    database.add_part(cpu1)
    database.add_part(cpu2)

    gpu1 = GPU("Nvidia RTX 3080", 800, "Nvidia", "10GB")
    gpu2 = GPU("AMD Radeon RX 6800", 700, "AMD", "16GB")
    database.add_part(gpu1)
    database.add_part(gpu2)
    try:
        cpu = database.get_part("Intel i7")
        if cpu:
            print(
                f"CPU: {cpu.get_name()}, Brand: {cpu.get_brand()}, Price: {cpu.get_price()}"
            )

        all_parts = database.get_all_parts()
        for part in all_parts:
            print(f"{part.get_name()}, Price: {part.get_price()}")

        database.update_part_price(name="Intel i7", new_price=3000)
    except PartNotFoundError as e:
        print(f'Error: {e}')

    print(
        f"CPU: {cpu.get_name()}, Brand: {cpu.get_brand()}, NEW Price: {cpu.get_price()}"
    )



    try:
        gpu = database.get_part("GTX 650")
        if gpu:
            print(f"GPU: {gpu.get_name()}, Brand: {gpu.get_brand()}")
    except PartNotFoundError as e:
        print(f'Error: {e}')

    try:
        cpu3 = CPU("AMD Ryzen 5", 250, "AMD", "3.8 GHz", "85W")
        database.add_part(cpu3)
    except DuplicatePartError as e:
        print(f'Error: {e}')


