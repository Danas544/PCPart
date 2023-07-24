import unittest
from main import CPU


class TestCPU(unittest.TestCase):
    def test_get_brand(self):
        cpu = CPU("Intel i7", 300, "Intel", "3.5 GHz", "95W")
        self.assertEqual(cpu.get_brand(), "Intel")

    def test_get_speed(self):
        cpu = CPU("Intel i7", 300, "Intel", "3.5 GHz", "95W")
        self.assertEqual(cpu.get_speed(), "3.5 GHz")

    def test_get_power_usage(self):
        cpu = CPU("Intel i7", 300, "Intel", "3.5 GHz", "95W")
        self.assertEqual(cpu.get_power_usage(), "95W")
