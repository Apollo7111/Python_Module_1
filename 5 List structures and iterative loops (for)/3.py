number = int(input('Write a number: '))
if number % 2 != 0 and number % 3 != 0 and number % 4 != 0 and number % 5 != 0 and number % 6 != 0 and number % 7 != 0 and number % 8 != 0 and number % 9 != 0 and number % 1 == 0 or number == 3 or number == 5 or number == 7:
    print('Its a prime number!')
else:
    print("Its NOT a prime number!")