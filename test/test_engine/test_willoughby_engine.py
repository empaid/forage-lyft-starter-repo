import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage=0
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage=0
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())