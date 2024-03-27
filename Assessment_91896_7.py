encrypt_decrypt = input("would you like encrypt a message or decrypt a message")

def encrypt(encryption):
  letters = {
      'a': 'd',
      'b': 'e',
      'c': 'f',
      'd': 'g',
      'e': 'h',
      'f': 'i',
      'g': 'j',
      'h': 'k',
      'i': 'l',
      'j': 'm',
      'k': 'n',
      'l': 'o',
      'm': 'p',
      'n': 'q',
      'o': 'r',
      'p': 's',
      'q': 't',
      'r': 'u',
      's': 'v',
      't': 'w',
      'u': 'x',
      'v': 'y',
      'w': 'z',
      'x': 'a',
      'y': 'b',
      'z': 'c'
  }

  for char in encryption:
      
      encrypted = ""

      if char.isalpha():
          is_upper = char.isupper()
          char = char.lower()
          encrypted_char = letters.get(char, char)
          
          if is_upper:
              translated_char = encrypted_char.upper()
          encrypted += translated_char
      
      else:
          encrypted += char

  return encrypted


if encrypt_decrypt == "decrypt" or "d":
    decryption = input("enter the message would you like to decrypt")

elif encrypt_decrypt == "encrypt" or "e":
    encryption = input("enter the message you would like to encrypt")


    translated = encrypt(encryption)
    print("your encrypted message is:", translated)