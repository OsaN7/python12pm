import os

if not os.path.exists('record.txt'):
    open('record.txt', 'w').close()

def register():
    print("=============Register=============")
    username = input('Enter username: ')
    username = username.lower()
    username = username.strip()
    if username in open('record.txt', 'r').read():
        print('Username already exists')
        exit()
    password = input('Enter password: ')
    password = password.strip()
    confirm_password = input('Confirm password: ')
    confirm_password = confirm_password.strip()
    if password != confirm_password:
        print('Password does not match')
        exit()

    with open('record.txt', 'a') as f:
        f.write(f'username:{username} password:{password}\n')
    print('Registered successfully')


def login():
    print("=============Login=============")
    username = input('Enter username: ')
    username = username.lower()
    username = username.strip()
    password = input('Enter password: ')
    password = password.strip()

    with open('record.txt', 'r') as f:
        find_users = []
        for user in f.readlines():
            find_users.append(user.split())
            
        x = 0
        total_user = len(find_users)
        login_success = False
        while x < total_user:
            uname = find_users[x][0][9:]
            upass = find_users[x][1][9:]
            if uname == username and upass == password:
                login_success = True
            x += 1

        if login_success:
            print(f'Welcome {username}')
        else:
            print('username or password is incorrect')

question = input('Do you have an account? (y/n): ')
question = question.lower()
if question == 'y':
    login()
elif question == 'n':
    register()
else:
    print('Invalid input')
    exit()

