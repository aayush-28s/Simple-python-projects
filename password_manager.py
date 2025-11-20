from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            try:
                user, psd = data.split('|')
                print("User :", user, "| Password :", fer.decrypt(psd.encode()).decode())
            except:
                print("[Error] Skipping invalid or corrupted line:", data)


def add():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    with open('password.txt','a') as f:
        f.write(username+'|'+fer.encrypt(password.encode()).decode()+'\n')

while True:
    mode = input('Would you like to view your password or add a password, or press x to exit (view/add/x)?: ').lower()

    if mode == 'x':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Please enter either view or add')
        continue