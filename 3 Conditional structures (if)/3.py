gender = input('What is your gender? (Female/Male)')
glLevels = float(input('What is your hemoglobin value?'))
if(gender == 'Female'):
    if(glLevels <117):
        print('Hemoglobin levels are too low!')
    if (glLevels > 155):
        print('Hemoglobin levels are too high!')
    if (glLevels >= 117 and glLevels <=155):
        print('Hemoglobin levels are normal :)')
elif(gender == 'Male'):
    if (glLevels < 134):
        print('Hemoglobin levels are too low!')
    if (glLevels > 167):
        print('Hemoglobin levels are too high!')
    if (glLevels >= 134 and glLevels <= 167):
        print('Hemoglobin levels are normal :)')