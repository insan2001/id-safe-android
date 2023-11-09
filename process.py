import Fernkey as fernkey
from cryptography.fernet import Fernet
import random

def encrypt(filename, password):
    key = Fernet.generate_key()
    encrypted_fernkey = fernkey.fernkey_encrypter(key, password)
    encrypter = Fernet(key)

    with open(filename, 'rb') as d:
        data = d.read()

    encrypted_data = encrypter.encrypt(data).decode("ascii")
    passwordrange = ""

    def find_number():
        password_range = random.randint(0, len(encrypted_data))
        num1, num2 = encrypted_data[(password_range-1)], encrypted_data[(password_range)]
        try:
            int(num1)
            int(num2)
            find_number()
        except ValueError:
            global passwordrange
            passwordrange = password_range

        password_range = int(passwordrange)
        encrypted_data_with_key = "{}{}{}".format(encrypted_data[:password_range],
                                                  encrypted_fernkey,
                                                  encrypted_data[password_range:])

        with open(filename, "w") as f:
            f.write(encrypted_data_with_key)

        with open("key.txt", "a+") as f:
            f.write(f"{key}\n")

    find_number()

def decrypt(key, regex_value, data_file):

    decrypter = Fernet(key)
    with open(data_file, 'r') as d:
        encrypted_data_with_key = d.read()

    values = encrypted_data_with_key.split(regex_value)

    encrypted_data = values[0] + values[1]
    normal_data = decrypter.decrypt(bytes(encrypted_data, "ascii"))
    filename = data_file

    with open(filename, 'wb') as f:
        f.write(normal_data)
