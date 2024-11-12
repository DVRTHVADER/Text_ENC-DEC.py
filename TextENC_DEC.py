alphabet = 'abcdefghijklmnopqrstuvwxyz'
num_letter = len(alphabet)

def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        char = char.lower()
        if char != ' ':
            index = alphabet.find(char)
            if index == -1:
                ciphertext += char
            else:
                new_index = (index + key) % num_letter
                ciphertext += alphabet[new_index]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        char = char.lower()
        if char != ' ':
            index = alphabet.find(char)
            if index == -1:
                plaintext += char
            else:
                new_index = (index - key) % num_letter
                plaintext += alphabet[new_index]
        else:
            plaintext += ' '
    return plaintext

print()
print('*** CAESAR CIPHER PROGRAM ***')
print()
print('Do you want to Encrypt or Decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPT SELECTED')
    print()
    key = int(input('Enter the Key (1 through 26): '))
    text = input('Enter text to Encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPT SELECTED')
    print()
    key = int(input('Enter the Key (1 through 26): '))
    text = input('Enter text to Decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
else:
    print("Invalid option selected. Please enter 'e' to encrypt or 'd' to decrypt.")
