""" Simple ecryption standard programm """
import random
import string
# Getting all string and numerics and symbols
all_char=string.ascii_letters + string.digits+ string.punctuation +" "
all_char=list(all_char)
key=all_char.copy()
# Shuffeling the list to get randomized text
random.shuffle(key)

# Encrypt
def encrypt():
    """ Looping for each letter in user input """
    global cipher
    print("Enter text to encrypt: ")
    user_input=input()
    cipher=""
    for letter in user_input:
        index=all_char.index(letter)
        cipher+=key[index]
    return cipher

# Decrypt
def decrypt(cipher):
    """ Looping for each letter in encrypterd text"""
    global decrypt
    decrypt=""
    for letter in cipher:
        dec_cipher=key.index(letter)
        decrypt+=all_char[dec_cipher]
    return decrypt
print("="*30)
encrypt()
print(f"You encypted words: {cipher}\n\n")
print("Enter text to decrypt: ")
user_dec=input()
decrypt(user_dec)
print(f"Your decrypted words: {decrypt}")
