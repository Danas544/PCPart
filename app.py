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


from pc_part import CPU, GPU
from error_exception import PartNotFoundError, DuplicatePartError
from pc_part_db import PCPartDatabase






if __name__ == "__main__":
    database = PCPartDatabase()

    cpu1 = CPU("Intel i7", 300, "Intel", "3.5 GHz", "95W")
    cpu2 = CPU("AMD Ryzen 5", 250, "AMD", "3.8 GHz", "85W")
    cpu5 = CPU("AMD Ryzen 6", 350, "AMD", "3.9 GHz", "90W")
    cpu6 = CPU("AMD Ryzen 7", 450, "AMD", "4.8 GHz", "120W")
    database.add_part(cpu1)
    database.add_part(cpu2)
    database.add_part(cpu5)
    database.add_part(cpu6)

    gpu1 = GPU("Nvidia RTX 3080", 800, "Nvidia", "10GB")
    gpu2 = GPU("AMD Radeon RX 6800", 700, "AMD", "17GB")
    gpu5 = GPU("AMD Radeon RX 6900", 800, "AMD", "18GB")
    gpu6 = GPU("AMD Radeon RX 7000", 900, "AMD", "19GB")
    gpu7 = GPU("Nvidia RTX 3090", 800, "Nvidia", "15GB")
    gpu8 = GPU("Nvidia RTX 4010", 900, "Nvidia", "18GB")
    gpu9 = GPU("Nvidia RTX 4050", 100, "Nvidia", "22GB")
    database.add_part(gpu1)
    database.add_part(gpu2)
    database.add_part(gpu5)
    database.add_part(gpu6)
    database.add_part(gpu7)
    database.add_part(gpu8)
    database.add_part(gpu9)

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
        print(f"Error: {e}")

    print(
        f"CPU: {cpu.get_name()}, Brand: {cpu.get_brand()}, NEW Price: {cpu.get_price()}"
    )

    try:
        gpu = database.get_part("GTX 650")
        if gpu:
            print(f"GPU: {gpu.get_name()}, Brand: {gpu.get_brand()}")
    except PartNotFoundError as e:
        print(f"Error: {e}")

    try:
        cpu3 = CPU("AMD Ryzen 5", 250, "AMD", "3.8 GHz", "85W")
        database.add_part(cpu3)
    except DuplicatePartError as e:
        print(f"Error: {e}")

    try:
        cpu4 = CPU("Intel i9", 900, "Intel", "4.5 GHz", "120W")
        database.add_part(cpu4)
        database.update_cpu_brand("Intel i9", "Danieliaus BRANDAS BLYN")
    except DuplicatePartError as e:
        print(f"Error: {e}")
    except PartNotFoundError as e:
        print(f"Error: {e}")
    cpu = database.get_part("Intel i9")
    if cpu:
        print(
            f"CPU: {cpu.get_name()}, Brand: {cpu.get_brand()}, Price: {cpu.get_price()}"
        )

    try:
        gpu = database.get_part("Nvidia RTX 3080")
        database.update_cpu_brand("Nvidia RTX 3080", "Noriu klaidu")
    except TypeError as e:
        print(f"Error: {e}")

    amd_cpus = database.filter_cpus_by_brand("AMD")
    for cpu in amd_cpus:
        print(
            f"CPU: {cpu.get_name()}, Brand: {cpu.get_brand()}, Price: {cpu.get_price()}"
        )

    nvidia_gpus = database.filter_gpus_by_brand("Nvidia")
    for gpu in nvidia_gpus:
        print(
            f"GPU: {gpu.get_name()}, Brand: {gpu.get_brand()}, Price: {gpu.get_price()}"
        )

    amd_gpus = database.filter_gpus_by_brand("AMD")
    for gpu in amd_gpus:
        print(
            f"GPU: {gpu.get_name()}, Brand: {gpu.get_brand()}, Price: {gpu.get_price()}"
        )

    amd_cpus_dict = database.get_cpus_by_brand_dict("AMD")
    print("Parsed CPUs by brand 'AMD':", amd_cpus_dict)

    nvidia_gpus_dict = database.get_gpus_by_brand_dict("Nvidia")
    print("Parsed GPUs by brand 'Nvidia':", nvidia_gpus_dict)
