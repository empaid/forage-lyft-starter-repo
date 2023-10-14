import unittest
from datetime import date

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.8, 0.9, 1, 0.8]
        tires = OctoprimeTires(tire_wear_array)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.7, 0.7, 0.7, 0.8]
        tires = OctoprimeTires(tire_wear_array)
        self.assertFalse(tires.needs_service())