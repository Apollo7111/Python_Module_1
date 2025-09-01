# seasons = {'Spring': [3,4,5] ,
#            'Summer': [6,7,8],
#            'Autumn': [9,10,11],
#            'Winter': [12,1,2]}
seasons = ("Spring", "Summer", "Autumn", "Winter")
inpt = int(input('Enter a number: '))
if (inpt in range(3,6)):
    print(seasons[0])
elif(inpt in range(6,9)):
    print(seasons[1])
elif (inpt in range(9, 12)):
    print(seasons[2])
elif (inpt in range(1, 3) or inpt == 12):
    print(seasons[3])
