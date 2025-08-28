import random
def dice ():
    return random.randint(1, 6)
while (True):
    a = dice()
    print(a)
    if(a == 6):
        break;