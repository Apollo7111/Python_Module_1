number = input('Enter a number: ')
largest = 0
smallest = int(number)
while(number != ''):
    if(int(number) > largest):
        largest = int(number)
    if(int(number) < smallest):
        smallest = int(number)
    number = input('Enter a number: ')
print(f"Smallest number - {smallest} "
      f"Largest number - {largest}")