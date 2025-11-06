from random import randint


class Car:
    def __init__(self, regNumber, maxSpeed, currSpeed = 0, travelledDistance = 0):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.currSpeed = currSpeed
        self.travelledDistance = travelledDistance

    def accelerate(self, speed):
        speedChange = self.currSpeed + speed
        if speedChange > self.maxSpeed:
            self.currSpeed = self.maxSpeed
        elif speedChange < 0:
            self.currSpeed = 0
        else:
            self.currSpeed = speedChange

    def drive(self, hours):
        if not hours <= 0:
            self.travelledDistance += self.currSpeed * hours

class ElectricCar(Car):
    def __init__(self, regNumber, maxSpeed, battery):
        self.battery_capacity = battery
        super().__init__(regNumber, maxSpeed)

class GasolineCar(Car):
    def __init__(self, regNumber, maxSpeed, tankVolume):
        self.tankVolume = tankVolume
        super().__init__(regNumber, maxSpeed)

car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.3)


car1.accelerate(130)
car2.accelerate(150)
car1.drive(3)
car2.drive(3)

print(f'car1: {car1.travelledDistance}x km')
print(f'car2: {car2.travelledDistance}km')


