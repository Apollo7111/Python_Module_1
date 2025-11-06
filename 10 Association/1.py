class Elevator:
    def __init__(self, bottomFloor, topFloor, currFloor = 0):
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor
        self.currFloor = bottomFloor


    def go_to_floor(self, floor):
        if(floor > 0):
            for i in range(floor):
                Elevator.floor_up(self)
        else:
            for i in range(floor):
                Elevator.floor_down(self)
    def floor_up(self):
        if(self.currFloor == self.topFloor):
            return
        self.currFloor += 1
        print(f'Current floor is {self.currFloor}')
    def floor_down(self):
        if(self.currFloor == self.bottomFloor):
            return
        self.currFloor -= 1
        print(f'Current floor is {self.currFloor}')


h = Elevator(2, 10)

h.go_to_floor(7)