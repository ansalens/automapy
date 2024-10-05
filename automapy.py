#! /usr/bin/python3
import sys
import webbrowser

try:   # try/except block for importing pyperclip module
    import pyperclip
except ImportError:   # If pyperclip was not found...
    print('Error - pyperclip module not found.')
    sys.exit()

try:   # try block for taking user's input for wishful location
    print("[*] Press q or type 'quit' to quit anytime")
    print("[*] Press only enter if you wish to copy the address from your clipboard")
    sys.argv = input('Enter address and city: ')

    # if user types quit or q program quits
    if sys.argv == 'quit' or sys.argv == 'q':
        sys.exit()
# except block for catching if user hits CTRL+C or CTRL+D
except (KeyboardInterrupt, EOFError):
    sys.exit(0)


# openGMaps is the main function
def open_GMAPS(args):
    while 1:
        try:
            if len(args) > 1:   # If length of arguments is greater than 1
                # Address variable is created where it stores all joined arguments together (user's input)
                address = ''.join(args[:])

            else:   # Otherwise when nothing is entered
                # it asks the user if it shall copy first item from his clipboard and store it into address variable
                copy = input("Copy location from clipboard? [Y/N]:")

                if copy.lower() in ["yes", "y"]:
                    address = pyperclip.paste()
                else:   # if user says anything else,loop breaks and function ends
                    break

            # Out of control-flow statements webbrowser's open function is called which will
            # open a browser with starting URL and append address variable to that URL
            webbrowser.open('https://www.google.com/maps/place/' + address)

            # again stores new location that user enters
            again = input('Enter another location: ').lower()
            # if user decides to press q or type quit program quits
            if again == 'q' or again == 'quit':
                sys.exit()
            # but if he typed anything else,args is assigned value of again
            if again != 'q' or again != 'quit':
                args = again
                continue   # Jumps back to start of loop with newly assigned args

            sys.exit()

        except (KeyboardInterrupt, EOFError):   # If user hits CTRL+C or CTRL+D
            sys.exit(0)


# Calling openGMaps function with sys.argv as the argument
open_GMAPS(sys.argv)

