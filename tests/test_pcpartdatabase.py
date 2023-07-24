import unittest
from main import PCPartDatabase, CPU, GPU


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
        part = self.database.get_part("no part")
        self.assertIsNone(part)

    def test_get_all_parts(self):
        all_parts = self.database.get_all_parts()
        self.assertEqual(len(all_parts), 4)

    def test_update_part_price_existing(self):
        part_name = "Intel i7"
        new_price = 320.0

        cpu = self.database.get_part(part_name)
        original_price = cpu.get_price()

        self.database.update_part_price(part_name, new_price)

        updated_cpu = self.database.get_part(part_name)
        self.assertEqual(updated_cpu.get_price(), new_price)
        self.assertNotEqual(updated_cpu.get_price(), original_price)

    def test_update_part_price_nonexistent(self):
        part_name = "No Part"
        new_price = 400.0

        self.database.update_part_price(part_name, new_price)

        part = self.database.get_part(part_name)
        self.assertIsNone(part)

if __name__ == "__main__":
    unittest.main()
