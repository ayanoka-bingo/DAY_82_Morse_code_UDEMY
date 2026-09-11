LETTER_CODE_DICT = {
    # Letters, numbers, special characters as key; code as value

    # LETTERS------------------------------------------
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": "." , "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",

    # NUMBERS------------------------------------------
    "1": ".----", "2": "..---", "3": "...--", 
    "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", 
    "0": "-----",

    # SPECIAL CHARACTERS------------------------------
    ",": "--..--", ".": ".-.-.-", "?": "..--..",
    ";": "-.-.-", ":": "---...", "/": "-..-.", 
    "-": "-....-", "'": ".----.", "(": "-.--.",
    ")": "-.--.-", "!": "-.-.--", '"':'.-..-.',  
}

CODE_LETTER_DICT = {
    # Code as key and letters, numbers, special characters as values
    code : letter for letter ,code in LETTER_CODE_DICT.items()
    
}



def decode(code:str)-> str: 
    """It helps to convert Morse code into English."""
    code_list = code.replace('/', '   ').split(sep="   ")
    word = ""
    for codes in code_list:
        new_code_list= codes.split(sep= " ")
        for itm in new_code_list:
            word += f"{CODE_LETTER_DICT[itm]}"
        word += " "
        
    return f"{word}"


def encode(text:str)-> str:
    """It helps to convert English into Morse code."""
    code =""
    for letter in text:
        if letter != " ":
            code += f"{LETTER_CODE_DICT[letter]} "
        else:
            code += " "*2
    return f"{code}"

is_cont = True




while is_cont:
    wish = input("What do you want : \ntype 'd' for decode,\ntype 'e' for encode:").lower()

    if wish == 'd':
        code = str(input('Code you want to convert into word:\t'))
        print(f'The word is: {decode(code)}\n')
    elif wish == 'e':
        word = input('word you want to convert into code:\t').upper()
        print(f'The code is: {encode(word)}\n')
    elif wish =='end':
        print("\033[31mENDING...\033[0m")
        is_cont = False
    else:
        print("\033[31mINPUT ERROR\033[0m")
    
