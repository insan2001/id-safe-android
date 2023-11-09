import passwordencrypter
import re

def fernkey_encrypter(fernkey, password):

    encrypted_password = passwordencrypter.encrypt_password(password)
    binary_fernkey = fernkey
    list_of_fernkey_value = list(binary_fernkey)

    final_values = []
    for key in list_of_fernkey_value:
        key = int(key)
        balance = encrypted_password % key
        times = encrypted_password // key
        one_key_value = f"{str(balance)}${str(times)}"
        final_values.append(one_key_value)

    encrypted_fernkey = ""
    for value in final_values:
        encrypted_fernkey += f"{value}&"

    return encrypted_fernkey


def fernkey_decrypter(encrypted_key, password):

    encrypted_password = passwordencrypter.encrypt_password(password)
    encrypted_values = encrypted_key.split("&")
    encrypted_values.pop(-1)

    decrypted_characters = []

    for value in encrypted_values:
        balance, times = value.split("$")
        encrypted_number = (encrypted_password - int(balance))/int(times)
        decrypted_character = chr(int(encrypted_number))
        decrypted_characters.append(decrypted_character)

    fernkey = ""
    for character in decrypted_characters:
        fernkey += character
    return fernkey

def fernkey_finder(file):

    try:
        with open(file, "r") as f:
            pattern = f.read()

        key_values = re.findall("\d*[&$]\d*", pattern)
        regex = "".join(key_values)
        return regex

    except UnicodeDecodeError:
        return None

def regex_to_key(data_file, password):
    regexvalue = fernkey_finder(data_file)

    for i in range(len(regexvalue)):
        if regexvalue[-i] == "&":
            print(i)
            print(regexvalue[:-i+1])
            if (-i + 1) != 0:
                re_regex = regexvalue[:-i+1]
                print(f"in loop {re_regex}")
                break
            else:
                re_regex = regexvalue
                break

    if regexvalue:
        key = fernkey_decrypter(regexvalue, password)
    else:
        key = None

    if key and len(key) == 44:
        return key, re_regex, data_file
    else:
        return False, None, None
