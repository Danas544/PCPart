from error_exception import PartNotFoundError, DuplicatePartError
from typing import Optional, List, Union, Dict
from pc_part import CPU, GPU
import logging
import logging.config


logging.config.fileConfig("logging_config.ini", disable_existing_loggers=False)

logger = logging.getLogger(__name__)


class PCPartDatabase:
    def __init__(self):
        self.parts = {}

    def add_part(self, part: Union[CPU, GPU]) -> None:
        part_name = part.get_name()
        if part_name in self.parts:
            logger.warning(f"Part '{part_name}' already exists in the database.")
            raise DuplicatePartError(
                f"Part '{part_name}' already exists in the database."
            )
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
        part.price = new_price
        logger.info(f"Updated the price of {name} to {new_price}.")

    def update_cpu_brand(self, name: str, new_brand: str) -> None:
        part = self.get_part(name)
        if isinstance(part, CPU):
            old_brand = part.brand
            part.brand = new_brand
            logger.info(
                f"Updated the brand of CPU '{name}' old brand: '{old_brand}' to '{part.brand}'."
            )
        elif part:
            raise TypeError(f"Part '{name}' is not a CPU.")

    def filter_cpus_by_brand(self, brand: str) -> List[CPU]:
        filtered_cpus = [
            part
            for part in self.parts.values()
            if isinstance(part, CPU) and part.get_brand() == brand
        ]
        return filtered_cpus

    def filter_gpus_by_brand(self, brand: str) -> List[GPU]:
        filtered_gpus = [
            part
            for part in self.parts.values()
            if isinstance(part, GPU) and part.get_brand() == brand
        ]
        return filtered_gpus

    def get_cpus_by_brand_dict(self, brand: str) -> Dict[str, float]:
        filtered_cpus = self.filter_cpus_by_brand(brand)
        return {cpu.get_name(): cpu.get_price() for cpu in filtered_cpus}

    def get_gpus_by_brand_dict(self, brand: str) -> Dict[str, float]:
        filtered_gpus = self.filter_gpus_by_brand(brand)
        return {gpu.get_name(): gpu.get_price() for gpu in filtered_gpus}
