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

raceFinished = False
carList = []
for i in range(1, 11):
    carList.append('car_{}'.format(i))
    carList[i-1] = Car(f'ABC-{i}', randint(100, 200))
    carList[i-1].winner = ''


while not raceFinished:
    for i in carList:
        i.accelerate(randint(-10, 15))
        i.drive(1)
        if(i.travelledDistance >= 10000):
            print(f'The race has finished! The car with registration number {i.regNumber} won!')
            i.winner = '# Winner '
            raceFinished = True
            break;

for i in carList:
    print(f'{i.winner}Car {carList.index(i)+1}: Registration number: {i.regNumber}, Maximum speed: {i.maxSpeed}km/h, Current speed: {i.currSpeed}km/h, Distance travelled {i.travelledDistance}km')

    if(carList.index(i)+1 == 10):
        break;
    else:
        print('―' * 73)

