import unittest
from main import PCPartDatabase, CPU ,GPU 


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



if __name__ == "__main__":
    unittest.main()
