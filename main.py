import os
import time

def clear_screen():
    os.system("clear")

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

    

    if (choice == "3"):
        clear_screen()
        print("Thanks for using BudgetBuddy!!")
        wait_for(1)
        clear_screen()
        break