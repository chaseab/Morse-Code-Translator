#This is a Morse Code Translator
def encyption(text)
    morse_code = {' ': '| ', 'a': '. _ ', 'b': '_ . . . ', 'c': '_ . _ . ', 'd': ' _ . . ', 'e': '. ', 'f': '. . _ .', 'g': '_ _ .', 'h': '. . . . ', 'i': '. . ', 'j': '. _ _ _ ', 'k': '_ . _ ', ' l': '. _ . . ', 'm': '_ _ ', 'n': '_ . ', 'o': '_ _ _ ', 'p': '. _ _ . ', 'q': '_ _ . _ ', 'r': '. _ . ', 's': '. . . ', 't': '_ ', 'u': '. . _ ', 'v': '. . . _ ', 'w': '|', 'x': '|', 'y': '|', 'z': '|', '1': '|', '2': '|', '3': '|', '4': '|', '5': '|', '6': '|', '7': '|', '8': '|', '9': '|', '0': '|'}
i = input('Would you like to decypher or encrypt text? ').lower
if i == "encrypt":
    x = input('Please type in the text you would like to encrypt. ')

if i == "decypher":
    x = input('Please type in the text you would like to decypher. ')
