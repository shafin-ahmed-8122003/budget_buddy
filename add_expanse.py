from clear_screen import *

def add_expanse():
    while True:
        clear_screen()
        print("Add an expanse")
        choice = input("> ")

        if choice == "q":
            clear_screen()
            break