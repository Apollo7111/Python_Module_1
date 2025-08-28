def func (a):
    numsum = 0
    for number in a:
        numsum += number
    return numsum

list = []

while True:
    inpt = input('Enter a number, leave an empty space to finish the list: ')
    if(inpt == ''):
        break;
    else:
        list.append(int(inpt))

print(func(list))

