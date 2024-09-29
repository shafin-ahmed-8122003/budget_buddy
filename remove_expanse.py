from clear_screen import *

def remove_expanse():
    while True:
        clear_screen()
        print("Remove an expanse")
        choice = input("> ")

        if choice == "q":
            clear_screen()
            break