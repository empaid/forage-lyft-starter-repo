import unittest
from datetime import date

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.8, 0.9, 1, 0.8]
        tires = CarriganTires(tire_wear_array)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.8, 0.8, 0.7, 0.6]
        tires = CarriganTires(tire_wear_array)
        self.assertFalse(tires.needs_service())