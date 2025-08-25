import random
dices = int(input('How many dices should we roll?'))
sum = 0
for i in range(dices):
    sum += random.randint(1,6)
print(sum)