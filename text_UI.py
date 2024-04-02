# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nicholas Dorscht"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298132"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-013"

#==========================================#
# Place your script for your text_UI after this line

from histogram import histogram
from curve_fit import curve_fit

BOLDON = '\033[1m'
BOLDOFF = '\033[0m'

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
                            
while True :
    print(f"The available commands are:\n\t{BOLDON}L){BOLDOFF}oad Data\n\t{BOLDON}S){BOLDOFF}ort Data\n\t{BOLDON}C){BOLDOFF}urve Fit\n\t{BOLDON}H){BOLDOFF}istogram\n\t{BOLDON}E){BOLDOFF}xit\n\n")
    user_choice = input("Please type your command: ").lower()
    
    if user_choice == 'l' :
        file = input("Please enter the name of the file: ")
        
        valid_attributes = ["Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Armor", "Weapon", "Health", "All"]
        
        valid = False
        
        # Chack for valid attribute
        while not valid :
            attribute = input("Please enter an attribute to use as a filter: ")
            
            if attribute in valid_attributes :
                valid = True
        
        attribute_value = ""
        # Get value if attribute isn't "All"
        if not (attribute == "All") :
            attribute_value = input("Please enter the value of the attribute: ")
            
        character_data = load_data(file, attribute, attribute_value)

        print("Data Loaded")
        
    elif user_choice == 's' :
        
        print("Please enter the attribute you want to use for sorting: ")
        attribute = input("'Agility', 'Armor', 'Intelligence', 'Health': ")
    
        valid_attributes = ['Agility', 'Armor', 'Intelligence', 'Health']
        while not(attribute in valid_attributes) :
            print("Invalid command.")
            attribute = input("'Agility', 'Armor', 'Intelligence', 'Health': ")
            
        order = input(f"Ascending ({BOLDON}A{BOLDOFF}) or Descending ({BOLDON}D{BOLDOFF}) order: ")
        
        try :
            sort_data(character_data, order, attribute)
            display_data = input("Data Sorted. Do you want to display the Data?: ")
        except :
            print("File not loaded. Please, load a file first.")
            continue
                    
        if display_data == "Y" :
            print(character_data)
            
    elif user_choice == 'c' :
        
        attribute = input("Please enter the attribute you want to use for plotting: ")
        valid_attributes = ['Agility', 'Armor', 'Intelligence', 'Health']
        while not(attribute in valid_attributes) :
            print("Invalid command.")
            attribute = input("'Agility', 'Armor', 'Intelligence', 'Health': ")
        
        deg = input("Please enter the order of the polynomial to be fitted: ")
        try :
            print(curve_fit(character_data, attribute, int(deg)))
        except :
            print("File not loaded. Please, load a file first.")
            continue
        
    elif user_choice == 'h' :
        
        attribute = input("Please enter the attribute you want to use for plotting: ")
        valid_attributes = ['Agility', 'Armor', 'Intelligence', 'Health']
        while not(attribute in valid_attributes) :
            print("Invalid command.")
            attribute = input("'Agility', 'Armor', 'Intelligence', 'Health': ")
        
        try :
            histogram(character_data, attribute)
        except :
            print("File not loaded. Please, load a file first.")
            continue
        
    elif user_choice == 'e' :
        break