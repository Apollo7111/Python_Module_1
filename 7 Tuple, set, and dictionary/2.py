names = set({})
while True:
    inpt = input('Enter a name: ')
    if(inpt == ''):
        break;
    if(inpt in names):
        print(f'Existing name {inpt}')
    else:
        {names.add(inpt)}
        print(f'New name: {inpt}')
for name in names:
    print(name);
