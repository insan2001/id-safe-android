def encrypt_password(passwd):
    password = bytes(passwd, 'ascii')
    length = len(passwd)

    value = 0

    for i, letter in zip(range(1, length+1), password):
        result = int(letter) * i
        value += result

    return int(value)
