# Imports
import sys, os      # for file stuff
import enum         # cause I like having enums and wtf are they not native?!
import csv          # making csv file handling amillion times easier
import tempfile     # write is done immediately, this is to basically store a buffer
## High Level Variables
file_path = ""
create_new = True
new_file_name = ""
tf1_name = ""
tf2_name = ""
#############################
## File functions
#############################
## Opens the file in the correct form
def open_file():
    global tf1_name
    # open file
    f = open(file_path, "rb")
    # create temp file
    tf = tempfile.NamedTemporaryFile(prefix="DataCleanerWorkingFile_",
                                            suffix="",
                                            dir="",
                                            delete=False)
    # copy file contents to tempfile
    for line in f.readlines():
        tf.write(line)
    # close the real file
    f.close()
    # reset cursor for temp file
    global tf1_name
    tf1_name = tf.name
    tf.close()    
## Save file function
def save_file():
    global tf1_name
    global tf2_name
    if (create_new):
        f = open(new_file_name, "w")
    else:
        f = open(file_path, "w")
    tf = open(tf1_name, "r")
    for line in tf.readlines():
        f.write(line)
    f.close()
    tf.close()
#############################
## Operation Functions
#############################
def remove_data_column():
    global tf1_name
    global tf2_name
    print("REMOVE DATA COLUMN")
    print("1 - Remove by Index")
    print("2 - Remove by Field Name")
    method = input("Select an option from above (invalid will return to menu): ").upper()  
    # set up temp file
    tf1 = open(tf1_name, "r")
    reader = csv.reader(tf1)
    tf = tempfile.NamedTemporaryFile(prefix="DataCleanerWorkingFile_",
                                            suffix="",
                                            dir="",
                                            delete=False)
    tf2_name = tf.name
    tf.close()
    tf2 = open(tf2_name, "w")
    writer = csv.writer(tf2)
    # select method
    if (method == "1"):
        index_to_remove = int(input("enter the index to remove:\t"))
        for r in reader:
            row = []
            for i in range(len(r)):
                if (i != index_to_remove):
                    row.append(r[i])
            writer.writerow(row)
    elif (method == "2"):
        field_to_remove = input("enter the field to remove (case sensitive):\t")
        index_to_remove = 0
        header = True
        for r in reader:
            row = []
            if (header):
                for i in range(len(r)):
                    if (r[i] == field_to_remove):
                        index_to_remove = i
                header = False
            for i in range(len(r)):
                if (1 != index_to_remove):
                    row.append(r[i])
            writer.writerow(row)
    # delete tf1 and replace its var with tf2
    tf1.close()
    tf2.close()
    os.remove(tf1_name)
    tf1_name = tf2_name
#############################
## Menu Functions
#############################
def print_main_menu_options():
    print(  "   _____                        \n"+
            "  /     \   ____   ____  __ __  \n"+
            " /  \ /  \_/ __ \ /    \|  |  \ \n"+
            "/    Y    \  ___/|   |  \  |  / \n"+
            "\____|__  /\___  >___|  /____/  \n"+
            "        \/     \/     \/        ")
    print("1 - Remove Data Column")
    print("2 - Remove Data Row")
    print("S - Save Changes and Quit")
    print("Q - Quit Without Saving Changes")
## Menu function
def main_menu():
    do = True
    while(do):
        print_main_menu_options()
        action = input("Select an option from above: ").upper()
        if (action == "Q"):
            do = False
        elif (action == "S"):
            save_file()
            do = False
        elif (action == "1"):
            remove_data_column()
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
    file_path = input("Please enter the file you intend to modify (*.csv):\t")
    new_file_name = "new_dataset.csv"
    if (input("Do you want to create a new file? (Y/N Default: Yes):\t").upper() == "N"):
        create_new = False
    if (create_new):
        new_file_name = input("what would you like to name the file? (no extension):\t") + ".csv"
    if (os.path.isfile(file_path)):
        open_file()
        main_menu()
        os.remove(tf1_name)
        print("Closing the program!")
    else:
        print("File does not exist and cannot be opened")
