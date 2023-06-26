# make the alphabet into a variable
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)
user_input = ""
# functions go here:

# encrypt & decrypt text in one function.
def encrypt_decrypt(text, mode, key):
  result = ''
  if mode == 'd':
    key = -key

  for letter in text:
    letter = letter.lower()
    if not letter == ' ':
      index = letters.find(letter)
      if index == -1:
        result += letter
      else:
        new_index = index + key
        if new_index >= num_letters:
          new_index -= num_letters
        elif new_index < 0:
          new_index += num_letters
        result += letters[new_index]
  return result




# formatting of the program:
print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
while user_input=="":
 user_input = input().lower()
 

# final result at the end of the program:
 if user_input == 'e' or user_input ==  "encrypt":
  print('\nENCRYPTION MODE SELECTED')
  print()
  key = int(input('Enter the key(1 through 26): '))
  text = input('Enter the text to encrypt: ')
  ciphertext = encrypt_decrypt(text, user_input, key)
  print(f'CIPHERTEXT: {ciphertext}')

 elif user_input == 'd' or user_input == "decrypt":
  print('DECRYPTION MODE SELECTED')
  print()
  key = int(input('Enter the key (1 through 26): '))
  text = input('Enter the text to decrypt: ')
  plaintext = encrypt_decrypt(text, user_input, key)
  print(f'PLAINTEXT: {plaintext}')

 else:
  print("Please answer with e, d, encrypt or decrypt:")
  user_input=""
