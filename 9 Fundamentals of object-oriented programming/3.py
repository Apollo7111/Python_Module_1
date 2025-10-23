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

c1 = Car('ABC-123', 142)
print(f'Reg number: {c1.regNumber}\nmaxSpeed: {c1.maxSpeed}')
c1.accelerate(30)
c1.accelerate(70)
c1.accelerate(50)

print(f'Current Speed: {c1.currSpeed}')

c1.accelerate(-200)

print(f'Current Speed: {c1.currSpeed}')


c1.travelledDistance = 2000
c1.accelerate(60)
c1.drive(1.5)
print(f'Travelled distance: {c1.travelledDistance}')


