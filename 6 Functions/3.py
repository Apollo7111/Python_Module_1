def convert(gallon):
    return(gallon * 3.785)
while(True):
    inpt = int(input('Please input gallons or a negative number to exit: '))
    if(inpt < 0):
        print('Exiting...')
        break;
    else:
        print(f'{convert(inpt):.2f}L')