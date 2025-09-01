airports = {}
while True:
    opt = input('1 - Enter a new airport\n2 - Fetch information for an airport\n3 - Quit\n')
    match opt:
        case '1':
            airports.update({input('Enter the name of the Airport: '): input('Enter the ICAO code for the airport: ')})
            print('Airport successfully added')
        case '2':
            code = input('Please input the ICAO code for the airport: ')
            try:
                print(list(airports.keys())[list(airports.values()).index(code)])
            except:
                print('Invalid ICAO code!')
        case '3':
            print('Quitting...')
            break;
