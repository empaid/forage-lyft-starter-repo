from tires.tires import Tires
class OctoprimeTires(Tires):

    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return sum(self.tire_wear_array) >= 3