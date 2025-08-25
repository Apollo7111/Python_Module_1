fishLength = int(input('How long is your fish in cm?'))
if(fishLength >= 42):
    print('Your fish satisfies the size limit')
else:
    print(f"Fish isn't long enough, it needs additional {42 - fishLength} cm")