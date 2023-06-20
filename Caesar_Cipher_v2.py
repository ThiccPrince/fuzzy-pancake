letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, key):
  ciphertext = ''
  for letter in plaintext:
    letter = letter.lower()
    if not letter == ' ':
      index = letters.find(letter)
      if index == -1:
        ciphertext += letter
      else:
        new_index = index - key
        if new_index >= 26:
          new_index -= 26
        plaintext += letters[new_index]
  return plaintext

def decrypt(ciphertext, key):
  plaintext = ''
  for letter in plaintext:
    letter = letter.lower()
    if not letter == ' ':
      index = letters.find(letter)
      if index == -1:
        ciphertext += letter
      else:
        new_index = index + key
        if new_index < 0:
          new_index -= 26
        ciphertext += letters[new_index]
  return ciphertext

print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
  print('ENCRYPTION MODE SELECTED')
  print()
  key = int(input('Enter the key(1 through 26): '))
  text = input('Enter the text to encrypt: ')

elif user_input == 'd':
  print('DECRYPTION MODE SELECTED')
  print()
  key = int(input('Enter the key (1 through 26): '))
  text = input('Enter the text to decrypt: ')
