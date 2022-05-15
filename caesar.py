def encrypt(key, plaintext):
    ciphertext = ""

    for c in plaintext:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the key
            new_index = (c_index + key) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to encrypted string
            ciphertext = ciphertext + new_character

        else:

            # since character is not uppercase, leave it as it is
            ciphertext += c

    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""

    for c in ciphertext:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the key
            new_index = (c_index - key) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to encrypted string
            plaintext = plaintext + new_character

        else:

            # since character is not uppercase, leave it as it is
            plaintext = plaintext + c

    return plaintext
