import unittest
from pc_part import GPU


class TestGPU(unittest.TestCase):
    def test_get_brand(self):
        gpu = GPU("Nvidia RTX 3080", 800, "Nvidia", "10GB")
        self.assertEqual(gpu.get_brand(), "Nvidia")

    def test_get_memory(self):
        gpu = GPU("Nvidia RTX 3080", 800, "Nvidia", "10GB")
        self.assertEqual(gpu.get_memory(), "10GB")
