import unittest
from src.systems.metabolism.data_processing import DataMetabolism

class TestMetabolism(unittest.TestCase):
    def test_energy_consumption(self):
        metabolism = DataMetabolism()
        initial_energy = metabolism.atp_level
        metabolism.digest_data([1,2,3])
        self.assertLess(metabolism.atp_level, initial_energy)
