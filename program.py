##########################
##Dice Roller
##Authour: Oguzhan Mclaren https://github.com/Mini413
##Version: 0.0.1
##Last updated: 14/6/2022
##########################

#Libraries
from optparse import Option
from os import system
from enum import Enum
import random
from abc import abstractmethod
from dataclasses import dataclass

# Enumerator list for menu options
# Comment for future Oguzhan. Enumerators have further methods that are used to display their name (.name) or value (.value)
class Options(Enum):
    MODE1 = "1"
    QUIT = "2"

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

# A menu that the user can select options from
@dataclass
class Menu():
    title: str
    mode1: str 
    quit: str

    def clear_screen(self):
        system("cls")

    def gui_layout(self):
        print(f"##### {self.title} #####\n{Options.MODE1.value}) {self.mode1}\n{Options.QUIT.value}) {self.quit}")

    def get_user_selection(self):
        return input("Please select an option >> ")

### Main ###
menu = Menu("Dice Roller", "Roll some dice", "Quit")
val = " "
menu.clear_screen()

while val != Options.QUIT.value:
    menu.gui_layout()
    val = menu.get_user_selection()

    if val == Options.MODE1.value:
        print("New Mode")
    elif val == Options.QUIT.value:
        print("Thank you for playing!")
    else:
        menu.clear_screen()
        print("!!PLEASE SELECT A VALID OPTION!!")

    
