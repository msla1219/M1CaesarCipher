def encrypt(key, plaintext):
    ciphertext = ""

    # loop to encrypt one character by character
    for each_char in plaintext:

        # only in case of uppercase
        if each_char.isupper():

            # store the offset (relative position) from "A"
            offset = ord(each_char) - ord("A")

            # move the position by the key
            new_offset = (offset + key) % 26

            # append to encrypted character to the string under the encryption
            ciphertext = ciphertext + chr(ord("A") + new_offset)

        # just do nothing in case of not uppercase
        else:
            ciphertext = ciphertext + each_char

    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""

    # loop to decrypt one character by character
    for each_char in ciphertext:

        # only in case of uppercase
        if each_char.isupper():

            # store the offset (relative position) from "A"
            offset = ord(each_char) - ord("A")

            # move the position reversely by the key
            new_offset = (offset - key) % 26

            # append to decrypted character to the string under the decryption
            plaintext = plaintext + chr(ord("A") + new_offset)

        # just do nothing in case of not uppercase
        else:
            plaintext = plaintext + each_char

    return plaintext
