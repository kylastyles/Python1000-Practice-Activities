""" 
File: PR05_MenuChoices.py
Requirements: PT05_MenuChoices.pdf
"""

# TODO: Your solution goes here!

#!usr/bin/env python3
from datetime import datetime, date, time

# Problem Domain: Textual User Interface ("TUI")
# Mission Summary: Create an "Input Option Loop"

# BANNER FUNCTIONS
def show_stars(num):
    return "\t" + ("*" * num)

def make_banner(message):
    x = len(message)
    stars = show_stars(x + 4)
    print(stars)
    print("\t* " + message + " *")
    print(stars)

# GREETING
print("WELCOME to PRO5!\n\n\n")

# MENU_CHOICES
menu_options = ["Display Custom Banner", "Display Default Banner", "Quit Program"]

def show_menu(menu_options):
    for index,option in enumerate(menu_options, 1):        
        print(str(index) + ".) " + option)
    return "\n"

# MENU_SELECTION
def run_program():
    while True:

        user_choice = input(show_menu(menu_options))

        if user_choice == "1":
            d = datetime.now()
            make_banner(str(d))
            continue
        elif user_choice == "2":
            make_banner("Hello User!")
            continue
        elif user_choice == "3":
            break
        else:
            print("Bad Choice\n")
            continue


run_program()
