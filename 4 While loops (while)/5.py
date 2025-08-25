username = input('Username: ')
password = input('Password: ')
tries = 0
while True:
    if(tries > 5):
        print('Access denied')
        break;
    if(username == 'python' and password == 'rules'):
        print("Welcome")
        break;
    username = input('Username: ')
    password = input('Password: ')
    tries += 1

