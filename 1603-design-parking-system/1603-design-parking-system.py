class ParkingSystem:
    def __init__(self, big, medium, small):
        self.system = {1: big, 2: medium, 3: small}
 
    def addCar(self, carType):
        if self.system[carType] == 0:
            return False
        elif self.system[carType] > 0:
            self.system[carType] -= 1
            return True