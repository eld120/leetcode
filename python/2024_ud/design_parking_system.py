




class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # self.big = 1
        # self.medium = 2
        # self.small = 3
        self._spots = {
            1 : big,
            2 : medium,
            3 : small
                       }

    def addCar(self, carType: int) -> bool:
        try:
            if self._spots[carType] > 0:
                self._spots[carType] -= 1
                return True
            return False
        except KeyError:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


def test_one():
    system = ParkingSystem(1,1,0)
    system.addCar(1) == True
    system.addCar(2) == True
    system.addCar(3) == False
    system.addCar(1) == False