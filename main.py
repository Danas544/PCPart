
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



class PCPart:
    def __init__(self, name, price, color=None):
        self.name = name
        self.price = price
        self.color = color

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color


class CPU(PCPart):
    def __init__(self, name, price, brand, speed, power_usage, color=None):
        super().__init__(name, price, color)
        self.brand = brand
        self.speed = speed
        self.power_usage = power_usage

    def get_brand(self):
        return self.brand

    def get_speed(self):
        return self.speed

    def get_power_usage(self):
        return self.power_usage


class GPU(PCPart):
    def __init__(self, name, price, brand, memory, color=None):
        super().__init__(name, price, color)
        self.brand = brand
        self.memory = memory

    def get_brand(self):
        return self.brand

    def get_memory(self):
        return self.memory
    

class PCPartDatabase:
    def __init__(self):
        self.parts = {}

    def add_part(self, part):
        self.parts[part.get_name()] = part

    def get_part(self, name):
        return self.parts.get(name, None)

    def get_all_parts(self):
        return list(self.parts.values())
    

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


    cpu = database.get_part("Intel i7")
    if cpu:
        print(f"CPU: {cpu.get_name()}, Brand: {cpu.get_brand()}, Price: {cpu.get_price()}")

    all_parts = database.get_all_parts()
    for part in all_parts:
        print(f"{part.get_name()}, Price: {part.get_price()}")