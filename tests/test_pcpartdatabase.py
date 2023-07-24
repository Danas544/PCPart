import unittest
from main import PCPartDatabase, CPU, GPU
from error_exception import PartNotFoundError, DuplicatePartError


class TestPCPartDatabase(unittest.TestCase):
    def setUp(self):
        self.database = PCPartDatabase()

        cpu1 = CPU("Intel i7", 300, "Intel", "3.5 GHz", "95W")
        cpu2 = CPU("AMD Ryzen 5", 250, "AMD", "3.8 GHz", "85W")
        self.database.add_part(cpu1)
        self.database.add_part(cpu2)

        gpu1 = GPU("Nvidia RTX 3080", 800, "Nvidia", "10GB")
        gpu2 = GPU("AMD Radeon RX 6800", 700, "AMD", "16GB")
        self.database.add_part(gpu1)
        self.database.add_part(gpu2)

    def test_get_part(self):
        cpu = self.database.get_part("Intel i7")
        self.assertIsNotNone(cpu)
        self.assertEqual(cpu.get_name(), "Intel i7")
        self.assertEqual(cpu.get_brand(), "Intel")
        self.assertEqual(cpu.get_price(), 300)

    def test_get_part_not_exist(self):
        with self.assertRaises(PartNotFoundError) as cm:
            self.database.get_part("no part")
        exception = cm.exception
        self.assertEqual(str(exception), "Part 'no part' not found in the database.")

    def test_get_all_parts(self):
        all_parts = self.database.get_all_parts()
        self.assertEqual(len(all_parts), 4)

    def test_update_part_price_existing(self):
        part_name = "Intel i7"
        new_price = 320.0
        self.database.update_part_price(part_name, new_price)
        cpu = self.database.get_part(part_name)
        self.assertEqual(cpu.get_price(), new_price)

    def test_update_part_price_nonexistent(self):
        part_name = "No Part"
        new_price = 400.0
        with self.assertRaises(PartNotFoundError) as cm:
            self.database.update_part_price(part_name, new_price)
        exception = cm.exception
        self.assertEqual(str(exception), "Part 'No Part' not found in the database.")

    def test_add_part_duplicate(self):
        cpu3 = CPU("AMD Ryzen 5", 260.0, "AMD", "3.7 GHz", "90W")
        with self.assertRaises(DuplicatePartError) as cm:
            self.database.add_part(cpu3)
        exception = cm.exception
        self.assertEqual(str(exception), "Part 'AMD Ryzen 5' already exists in the database.")


if __name__ == "__main__":
    unittest.main()
