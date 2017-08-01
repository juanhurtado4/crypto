def alphabet_position(letter):
    # Function finds index of letter in alphabet
    if letter.isupper() == True:
        return ord(letter) - 65
    else:
        return ord(letter.lower()) - 97

def rotate_character(char, e_key):
    # Function rotates letter to encrypt
    pos_char = alphabet_position(char)
    if type(e_key) == int:
        pos_sig = int(e_key)
    else:
        pos_sig = alphabet_position(e_key)
    if char.isupper() == True:
        if pos_char + pos_sig > 25:
            return chr(((pos_char + pos_sig) % 26) + 65)
        else:
            return chr((pos_char + pos_sig) + 65)
    else:
        if pos_char + pos_sig > 25:
            return chr(((pos_char + pos_sig) % 26) + 97) # If after rotation, index is greater than the len(alphabet): rotate
        else:
            return chr((pos_char + pos_sig) + 97) # Else add rotation to letter