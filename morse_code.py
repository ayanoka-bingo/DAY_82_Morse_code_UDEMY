# code = input("What do you want : \ntype 'd' for decode,\ntype 'e' for encode:").lower()

letter_dict = {
    ""
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
    
