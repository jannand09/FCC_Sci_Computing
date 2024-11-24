# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:11:27 2024

@author: janna
"""

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)


# custom_key = 'python'

# def vigenere(message, key):
#     key_index = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     encrypted_text = ''

#     for char in message.lower():
    
#         # Append space to the message
#         if char == ' ':
#             encrypted_text += char
#         else:        
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1

#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
    
#     return encrypted_text
    
# encryption = vigenere(text, custom_key)


text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
