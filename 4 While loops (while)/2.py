i = 1
while(i >= 0):
    centimeters = int(input('Enter a positive number: '))
    i = centimeters
    if (i < 0):
        print('Negative number detected!\nTerminating program...')
        break
    print(f'{centimeters} cm = {centimeters * 0.3937} inch')