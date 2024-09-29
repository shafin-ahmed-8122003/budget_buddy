import time
from add_expanse import *
from remove_expanse import *
from clear_screen import *

def wait_for(seconds):
    time.sleep(seconds)

while True:
    clear_screen()

    print("Welcome to BudgetBuddy!")
    print()

    print("1. Add an expanse")
    print("2. Remove an expanse")
    

    print()
    print("3. Exit")
    print()

    choice = input("> ")

    if choice == "1":
        add_expanse()
    
    if choice == "2":
        remove_expanse()

    if (choice == "3"):
        clear_screen()
        print("Thanks for using BudgetBuddy!!")
        wait_for(1)
        clear_screen()
        break