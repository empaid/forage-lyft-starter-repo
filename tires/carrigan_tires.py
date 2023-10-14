from tires.tires import Tires
class CarriganTires(Tires):

    def __init__(self, tire_wear_array: [int]):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return any(val>=0.9 for val in self.tire_wear_array)