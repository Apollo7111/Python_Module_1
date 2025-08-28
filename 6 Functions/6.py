import math
def pizza (cm, euro):
    pizzaRad = math.pi * cm
    return (euro / pizzaRad);


pizza1 = pizza(int(input('Enter cm for pizza 1: ')), int(input('Enter euro price for pizza 1: ')))
pizza2 = pizza(int(input('Enter cm for pizza 2: ')), int(input('Enter euro price for pizza 2: ')))
if(pizza1 < pizza2):
    print('Pizza 1 provides a better value for money')
else:
    print('Pizza 2 provides a better value for money')



