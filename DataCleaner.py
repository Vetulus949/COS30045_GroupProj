# Imports
import sys, os      # for file stuff
import enum         # cause I like having enums and wtf are they not native?!
import csv          # making csv file handling amillion times easier
import tempfile     # write is done immediately, this is to basically store a buffer
## High Level Variables
file_path = ""
create_new = True
new_file_name = ""
file = None
#############################
## Opens the file in the correct form
def open_file():
    if (create_new):
        file = open(file_path, "r")
    else:
        file = open(file_path, "rw")

#############################
## Menu Functions
#############################
def print_main_menu_options():
    print("1 - Remove Data Column")
    print("S - Quit and Save Changes")
    print("Q - Quit Without Saving Changes")
## Menu function
def main_menu():
    do = True
    while(do):
        print_main_menu_options()
        action = input("Select an option from above: ").upper()
        if (action == "Q"):
            do = False
#############################
## Saving Functions
#############################
def save_file():
    if (create_new):
        save_as_new()
    else:
        save_overwrite()
def save_as_new():
    pass
def save_overwrite():
    print("save overwrite not implemented :)")
#############################
## Entry point for program
#############################
if __name__ == "__main__":
    # for when you have more of a sense of aestetics than desire for intelligent design
    print("\n______      _          _____ _                            \n" +
            "|  _  \    | |        /  __ \ |                           \n" +
            "| | | |__ _| |_ __ _  | /  \/ | ___  __ _ _ __   ___ _ __ \n" +
            "| | | / _` | __/ _` | | |   | |/ _ \/ _` | '_ \ / _ \ '__|\n" +
            "| |/ / (_| | || (_| | | \__/\ |  __/ (_| | | | |  __/ |   \n" +
            "|___/ \__,_|\__\__,_|  \____/_|\___|\__,_|_| |_|\___|_|   \n")
    file_path = input("Please enter the file you intend to modify (.csv):\t\t")
    new_file_name = "new_dataset.csv"
    if (input("Do you want to create a new file? (Y/N Default: Yes):\t\t").upper() == "N"):
        create_new = False
    if (create_new):
        new_file_name = input("what would you like to name the file? (no extension):\t\t") + ".csv"
    if (os.path.isfile(file_path)):
        main_menu()
        print("Closing the program!")
    else:
        print("File does not exist and cannot be opened")
