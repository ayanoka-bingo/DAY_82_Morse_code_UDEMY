# code = input("What do you want : \ntype 'd' for decode,\ntype 'e' for encode:").lower()

letter_dict = {
    # LETTERS
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": "." , "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",

    # NUMBERS
    "1": ".----", "2": "..---", "3": "...--", 
    "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", 
    "0": "-----",

    # SPECIAL CHARACTERS
    ",": "--..--", ".": ".-.-.-", "?": "..--..",
    ";": "-.-.-", ":": "---...", "/": "-..-.", 
    "-": "-....-", "'": ".----.", "(": "-.--.",
    ")": "-.--.-", "!": "-.-.--", '"':'.-..-.',  
}


def decode(code:str)-> str: 
    """It helps to convert Morse code into English."""
    for symbol in code:
        if symbol == ".":
            pass
    pass
def encode(text:str)-> str:
    """It helps to convert English into Morse code."""
    pass

code = ""


while code != 'end':
    code = input("What do you want : \ntype 'd' for decode,\ntype 'e' for encode:").lower()
    WORD = ""
    MORSE_CODE = ""

    if code == 'd':
        pass
    elif code == 'e':
        pass
    else:
        print("\033[31mINPUT ERROR\033[0m")
    
