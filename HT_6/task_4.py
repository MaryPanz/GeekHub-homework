morse = input("Morse: ")


def morse_code(morse):
    my_dict = { '.-': 'A', '-...': 'B':=,
   '-.-.': 'C', '-..': 'D', '.': 'E',
   '..-.': 'F', '--.': 'G', '....': 'H',
   '..': 'I', '.---': 'J', '-.-': 'K',
   '.-..': 'L', '--': 'M', '-.': 'N',
   '---': 'O', '.--.': 'P', '--.-': 'Q',
   '.-.': 'R', '...': 'S', '-': 'T',
   '..-': 'U', '...-': 'V', '.--': 'W',
   '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
   
    sentence = morse.split(" ")
    english = []  # Will contain English versions of letters
    for i in sentence:
        if i in my_dict:
            english.append(my_dict[i])
    return " ".join(english)
    
    
    
print(morse_code(morse))
