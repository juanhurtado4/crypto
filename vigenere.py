from helpers import alphabet_position, rotate_character

def encrypt(text, signature):
    # Function joins multiple encrypted characters together
    scramble = ''
    if len(signature) < 1:
        return text
    index = 0
    for character in text:
        if character.isalpha() == False:
            scramble += character
            continue
        elif index > len(signature)-1:
            scramble += rotate_character(character, signature[index % len(signature)])
            index += 1
        else:
            scramble += rotate_character(character, signature[index])
            index += 1
    return scramble

def main():
    msg = input('Enter msg you want to encrypt: ')
    rotate = input('Enter key: ')
    print(encrypt(msg, rotate))

if __name__=='__main__':
    main()