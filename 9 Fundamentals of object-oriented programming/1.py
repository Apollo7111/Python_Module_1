class Car:
    def __init__(self, regNumber, maxSpeed, currSpeed = 0, travelledDistance = 0):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.currSpeed = currSpeed
        self.travelledDistance = travelledDistance

c1 = Car('ABC-123', 142)
print(f'Reg number: {c1.regNumber}\nmaxSpeed: {c1.maxSpeed}')