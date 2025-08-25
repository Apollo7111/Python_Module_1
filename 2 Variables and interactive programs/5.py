import math
talents  = int(input('Enter talents: '))
pounds  = int(input('Enter pounds: '))
lots  = float(input('Enter lots: '))
convertedTalents = talents * 20
convertedPounds = (convertedTalents + pounds) * 32
convertedLots = (convertedPounds + lots) * 13.3 #grams
print(f'The weight in modern units:\n{int(convertedLots / 1000)} kilograms and { convertedLots - (int((convertedLots / 1000)) * 1000):.2f} grams.')