# made this because i had nothing else better to do
def main():
    morse_code_dictionary = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ',':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}

    options = {"option 1 ": "english > morse",
            "blank": "",
        "option 2 ": "morse > english"}

    def printoptions(options):
        for k,v in options.items():
            if "blank" in k:
                print()
            else:
                print(f"{k}{v}")

    printoptions(options)
    print("\n")

    user_choice = input("select an option (1/2)")

    if user_choice == "1":
        user_text = input("enter english: ").strip()
        morse_code = ""

        for character in user_text.upper():
            if character == " ":
                morse_code += "/ "
            else:
                morse_code += morse_code_dictionary[character] + " "

        print(morse_code)

    elif user_choice == "2":
        morse = input("enter morse: ")
        text = ""

        for part in morse.split(" "):
            if part == "/":
                text += " "
            elif part:
                idx = list(morse_code_dictionary.values()).index(part)
                text += list(morse_code_dictionary.keys())[idx]

        print(text)
    else:
        print("1/2 wasnt selected")

if __name__ == "__main__": # no need for this because no extra files but good practice
    while True:
        main()