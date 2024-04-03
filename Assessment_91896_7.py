#sequence: 2
#version: 6
#creator: Rylie Garner
#date: 22/3/2024
#purpose:to swap the letters in the encryption variable to letters which are 3 letters ahead in the alphabet and loops as many times as there are letters in the sentance in order to change every letter in the variable
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

    encrypted = ""

    for char in encryption:

        if char.isalpha():
            
            upper = char.isupper()
            char = char.lower()
            encrypted_char = letters.get(char, char)
            
            if upper:
            
                encrypted_char = encrypted_char.upper()
            
            encrypted += encrypted_char
        
        else:
            encrypted += char

    return encrypted

#sequence: 2
#version: 1
#creator: Rylie Garner
#date: 4/04/2024
#purpose: to swap the letters in the decryption variable to letters which are 3 letters behind in the alphabet and loops as many times as there are letters in the sentance in order to change every letter in the variable
def decrypt(decryption):
    letters = {
    'd': 'a',
    'e': 'b',
    'f': 'c',
    'g': 'd',
    'h': 'e',
    'i': 'f',
    'j': 'g',
    'k': 'h',
    'l': 'i',
    'm': 'j',
    'n': 'k',
    'o': 'l',
    'p': 'm',
    'q': 'n',
    'r': 'o',
    's': 'p',
    't': 'q',
    'u': 'r',
    'v': 's',
    'w': 't',
    'x': 'u',
    'w': 'v',
    'z': 'w',
    'a': 'x',
    'b': 'y',
    'c': 'z',
}
    decrypted = ""
    
    for char in decryption:
    
        if char.isalpha():

            upper = char.isupper()
            char = char.lower()
            decrypted_char = letters.get(char, char)

            if upper:

                decrypted_char = decrypted_char.upper()
            
            decrypted += decrypted_char
        
        else:
            decrypted += char
    
    return decrypted

#sequence: 1
#version: 4
#creator: Rylie Garner
#date: 4/04/2024
#purpose: to ask the user if they would like to encrypt or decrypt a message then run the defined function based off the users answers
encrypt_decrypt = input('would you like to encrypt or decrypt a message?')
encrypt_decrypt = encrypt_decrypt.lower

e_d = ['e', 'd', 'encrypt', 'decrypt']
while encrypt_decrypt not in e_d:
    encrypt_decrypt = input('please enter encrypt or decrypt')
    encrypt_decrypt = encrypt_decrypt.lower

if encrypt_decrypt in e_d:
    
    
    if encrypt_decrypt == 'e'or 'encrypt':
        encryption = input('type in the sentence you would like to encrypt:\n')
        encrypt(encryption)
    
    else:
        decryption = input('type in the sentance you would like to decrypt:\n')
        decrypt(decryption)
