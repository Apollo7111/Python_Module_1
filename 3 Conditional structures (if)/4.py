year = int(input('Please input a year: '))
if(year % 100 == 0):
    print("YEs")
    if (year % 4 == 0):
     print(f'Year {year} is a leap year ')