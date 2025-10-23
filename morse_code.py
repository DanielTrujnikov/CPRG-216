morseCode = {'A':'.-', 'B': '-...', 'C':'-.-.', 'D':'-..', 'E':'.',
             'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
             'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O': '---', 'P':'.--.',
             'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
             'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ',':',', ' ':' '} # added commas and spaces but not period since
# period can be interpreted as a morse code character (E).



user_input = input("Please write text that you would like translated to morse code\n")

morse_translation = ""                                         # to store the final morse code translation

for character in user_input.upper():                           # convert to uppercase to match keys in dictionary
    if character in morseCode:                                 # check if character is in the dictionary
        morse_translation += morseCode[character] + " "        # add morse code and a space
    else:
        morse_translation += "? "                              # for unknown characters

print("\nYour text in Morse code is:\n", morse_translation)    # print the final translation