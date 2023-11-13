from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # Remove trailing whitespaces
            if "|" not in data:
                continue  # Skip lines without "|"
            user, passw = data.split("|", 1)  # Split only at the first occurrence
            try:
                decrypted_pass = fer.decrypt(passw.encode()).decode()
                print('User', user, "| Password", decrypted_pass)
            except Exception as e:
                print(f"Error decrypting password for {user}: {str(e)}")


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + (fer.encrypt(pwd.encode())).decode() + '\n')


while True:
    mode = input("Would you like to add a new password or view existing ones (VIEW, ADD, QUIT): ")

    if mode.lower() == 'quit':  # Change 'q' to 'quit'
        break
    elif mode.lower() == 'view':
        view()
    elif mode.lower() == 'add':
        add()
    else:
        print("Invalid option")
        continue
