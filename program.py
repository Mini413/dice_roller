##########################
##Dice Roller
##Authour: Oguzhan Mclaren https://github.com/Mini413
##Version: 0.0.1
##Last updated: 15/6/2022
##########################

#Libraries
from os import system
from enum import Enum
import random
from abc import abstractmethod
from dataclasses import dataclass

# Enumerator list for menu options
# Comment for future Oguzhan. Enumerators have further methods that are used to display their name (.name) or value (.value)
class Options(Enum):
    MODE1 = "1"
    MODE2 = "2"
    MODE3 = "3"
    QUIT = "4"

# Dice options for the dice menu
class Dice_Options(Enum):
    DICE1 = "1"
    DICE2 = "2"
    DICE3 = "3"
    DICE4 = "4"
    DICE5 = "5"
    DICE6 = "6"
    BACK = "7"

# Interface that provides a method to create a layout in the terminal and clear the terminal
class Terminal_Format():
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def gui_layout():
        pass
    
    @abstractmethod
    def clear_screen():
        pass

# A menu that the user can select options from. This should be put into a separate file.
@dataclass
class Menu():
    title: str
    mode1: str
    mode2: str
    mode3: str 
    quit: str

    def clear_screen(self):
        system("cls")

    def gui_layout(self):
        print(f"##### {self.title} #####\n{Options.MODE1.value}) {self.mode1}\n{Options.MODE2.value}) {self.mode2}\n{Options.MODE3.value}) {self.mode3}\n{Options.QUIT.value}) {self.quit}")

    def get_user_selection(self):
        return input("Please select an option >> ")

    def option_validation(self, warn):
        system("cls")
        print(warn)


# Dice menu for the first mode of the initial menu. I didn't know how to inherit from a dataclass and using a dataclass as the __init__ sorta appends to each other, don't like it.
class Dice_Menu(Menu):
    def __init__(self, title, mode1, mode2, mode3, mode4, mode5, mode6, quit):
        super().__init__(title, mode1, mode2, mode3, quit)
        self.mode4 = mode4
        self.mode5 = mode5
        self.mode6 = mode6

    def gui_layout(self):
        print(f"##### {self.title} #####\n{Dice_Options.DICE1.value}) {self.mode1}\n{Dice_Options.DICE2.value}) {self.mode2}\n{Dice_Options.DICE3.value}) {self.mode3}\n{Dice_Options.DICE4.value}) {self.mode4}\n{Dice_Options.DICE5.value}) {self.mode5}\n{Dice_Options.DICE6.value}) {self.mode6}\n{Dice_Options.BACK.value}) {self.quit}")

# Allows for the creation of dices, was going to create separate classes for each different type of dice. Could be beneficial, not too sure.
class Dice():
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return random.randrange(1, self.faces + 1)

    def __str__(self):
        return f"d{self.faces}"

# Causal dice rolling mode that rolls the specified dice.
def casualDiceRolling():
    # Initialises the menu and clears the terminal
    casualRollMenu = Dice_Menu("Casual Roll", "4-sided dice", "6-sided dice", "8-sided dice", "10-sided dice", "12-sided dice", "20-sided dice", "Back")
    casualRollMenu.clear_screen()
    val1 = " "

    # Loop that runs the mode until the user wants to go 'BACK', rolls the specified dice
    while val1 != Dice_Options.BACK.value:
        # Shows the menu and stores the users selection
        casualRollMenu.gui_layout()
        val1 = casualRollMenu.get_user_selection()
        
        if val1 == Dice_Options.DICE1.value:
            d4 = Dice(4)
            casualRollMenu.clear_screen()
            print("Your {} rolled a... ".format(d4.__str__()), d4.roll())
        elif val1 == Dice_Options.DICE2.value:
            d6 = Dice(6)
            casualRollMenu.clear_screen()
            print("Your {} rolled a... ".format(d6.__str__()), d6.roll())
        elif val1 == Dice_Options.DICE3.value:
            d8 = Dice(8)
            casualRollMenu.clear_screen()
            print("Your {} rolled a... ".format(d8.__str__()), d8.roll())
        elif val1 == Dice_Options.DICE4.value:
            d10 = Dice(10)
            casualRollMenu.clear_screen()
            print("Your {} rolled a... ".format(d10.__str__()), d10.roll())  
        elif val1 == Dice_Options.DICE5.value:
            d12 = Dice(12)
            casualRollMenu.clear_screen()
            print("Your {} rolled a... ".format(d12.__str__()), d12.roll())
        elif val1 == Dice_Options.DICE6.value:
            d20 = Dice(20)
            casualRollMenu.clear_screen()
            print("Your {} rolled a... ".format(d20.__str__()), d20.roll())
        elif val1 == Dice_Options.BACK.value:
            break
        else:
            casualRollMenu.option_validation("!!PLEASE SELECT A VALID OPTION!!")

def doubleOrNothing():
    print("Hello")

# 
def trulyRandom():
    print("RANDOM")

# Main code of the program
def main():
    #Initialises the Menu and terminal
    menu = Menu("Dice Roller", "Casual Dice Roll", "Double or Nothing", "Truly Random", "Quit")
    val = " "

    # Creates a game loop that will end once the user quits from the program.
    while val != Options.QUIT.value:
        # Prints the menu and requets user input to determine what mode has been selected.
        menu.clear_screen()
        menu.gui_layout()
        val = menu.get_user_selection()

        # Runs the game mode functions according to the user input
        if val == Options.MODE1.value:
            casualDiceRolling()
        if val == Options.MODE2.value:
            doubleOrNothing()
        if val == Options.MODE3.value:
            trulyRandom()
        elif val == Options.QUIT.value:
            print("Thank you for playing!")
        else:
            menu.option_validation("!!PLEASE SELECT A VALID OPTION!!")

### Main ###
if __name__ == "__main__":
    main()