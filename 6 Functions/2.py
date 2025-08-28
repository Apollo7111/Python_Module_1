import random
inpt = int(input('Number of sides: '))
def dice ():
    return random.randint(1, inpt)
while (True):
    a = dice()
    print(a)
    if(a == inpt):
        break;