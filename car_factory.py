from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car import Car

from datetime import date

class ClassFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = (last_service_date, current_date)
        return Car(engine, battery)