# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nicholas Dorscht"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298132"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-013"

#==========================================#
from histogram import histogram
from curve_fit import curve_fit

def load_data(file_name: str, attribute: str, attribute_value) -> list[dict]:
    file = open(file_name, 'r')
    
    first_line = True
    result = []
    line_headers = []
    valid_attributes = ["Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Armor", "Weapon", "All"]
    
    if attribute in valid_attributes : 
        for line in file:
            line = line.strip().split(",")
            if first_line:
                first_line = False
                line_headers = line
            else :
                character = {}
                character[line_headers[0]] = line[0]
                character[line_headers[1]] = int(line[1])
                character[line_headers[2]] = int(line[2])
                character[line_headers[3]] = int(line[3])
                character[line_headers[4]] = int(line[4])
                character[line_headers[5]] = int(line[5])
                character[line_headers[6]] = float(line[6])
                character[line_headers[7]] = int(line[7])
                character[line_headers[8]] = line[8]
                
                health = (character["Strength"] + character["Agility"] + character["Stamina"] + character["Personality"] +
                    character["Intelligence"]) + (character["Armor"] ** 2 * character["Luck"])

                character["Health"] = health
                
                # Check if it should be added to list
                if attribute == "All" or character[attribute] == attribute_value :
                    result.append(character)
    else :
        return []
    
    return result

def sort_data(character_list: list[dict], order: str, attribute: str) -> None :
    switch = True
    if order == 'A':
        while switch:
            switch = False
            for i in range(len(character_list) - 1):
                
                    if character_list[i][attribute] > character_list[(i + 1)][attribute]:
                        reorder = character_list[i]
                        character_list[i] = character_list[i + 1]
                        character_list[i + 1] = reorder
                        switch = True
                            
    if order == 'D':
        while switch:
            switch = False
            for i in range(len(character_list) - 1):
                    if character_list[i][attribute] < character_list[(i + 1)][attribute]:
                        
                        reorder = character_list[i]
                        character_list[i] = character_list[i + 1]
                        character_list[i + 1] = reorder
                        switch = True

def run_commands(commands: list) -> None :
    for command in commands :
        if command[0] == 'l':
            character_data = load_data(command[1], command[2], command[3])
            print("Data Loaded")
            
        elif command[0] == 's' :
            sort_data(character_data, command[2], command[1])
            
            if command[3] == 'Y':
                print(character_data)
            else: 
                print("You selected to not display the data")
                
        elif command[0] == 'c' :
            print(curve_fit(character_data, command[1], int(command[2])))
        elif command[0] == 'h' :
            histogram(character_data, command[1])
        elif command[0] == 'e' :
            break
        
# Place your script for your batch_UI after this line
commands = []

#Load commands from batch file
file_name = input("Please enter the name of the file where your commands are stored: ")

file = open(file_name, 'r')

for line in file :
    line = line.strip().split(';')
    commands.append(line)

file.close()

# Run program with batch commands
run_commands(commands)