from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    # Function joins multiple encrypted characters together
    scramble = ''
    for character in text:
        if character.isalpha() == False:
            scramble += character
        else:
            scramble += rotate_character(character, rot)
    return scramble

def main():
    prompt = input('Enter a message: ')
    rotation = input('Rotate by: ')
    print(encrypt(prompt, rotation))

if __name__=='__main__':
    main()