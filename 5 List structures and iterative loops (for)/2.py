number = []
inputNumber = input('Enter a number: ')
while(inputNumber != ''):
    number.append(int(inputNumber))
    inputNumber = input('Enter a number: ')
number.sort(reverse=True)
for i in range(5):
    print(number[i])
