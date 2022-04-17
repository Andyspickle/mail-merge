#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
STARTING_LETTER = "./Input/Letters/starting_letter.txt"
INVITED_NAMES = "./Input/Names/invited_names.txt"
PLACEHOLDER = "[name]"


def read_file_lines(file: str):
    with open(file, "r") as f:
        return f.readlines()

def read_file(file: str):
    with open(file, "r") as f:
        return f.read()

def write_file(file: str):
    with open(file, "r") as f:
        return f.readlines()

def update_name(opened_letter: str, name: str):
    opened_letter.replace("[name]", name)
    return opened_letter


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(INVITED_NAMES, "r") as names_files:
    names = names_files.readlines()

