# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Evan Malott"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101300431"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-013"

#==========================================#
# Place your script for your text_UI after this line

from histogram import  histogram
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



while True: 
    valid_attributes = ["Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Armor", "Weapon", "All"]
    
    restart = True 
    if restart:
        restart = False #Will be set back to true of user makes error
    
        print("The available commands are: \nL)\nS)\nC)\nH)\nE)\n") #Display the user interface options 
        user_input = input("Please type your command: ") #take initial user command 
        user_input = user_input.lower() #make user_input lower case
        
    if user_input == 'l': #Load data
        
        file = input("Please enter the name of the file: ") #Get file name 
        #get attribute name 
      
        value = True
        while value: 
            attribute = input("Please enter the attribute to use as a filter: ") #Attribute to use for sorting 
            
            if attribute in valid_attributes: #check if attribute is valid 
                value = False #if valid stop asking 
            else:
                print('Invalid input')
        
        if attribute == 'All': #Check if attribute equal to all then set attribute value to all, which is handle in the load data function
            attribute_value = 'All'
        else:
            attribute_value = input("Please enter the value of the attribute: ") #get attribute value 
        
        if attribute != ('Occupation' and 'Weapon' and 'All'): #Check wether the attribute value will have a string value, if not convert input to a int 
            attribute_value = int(attribute_value) 
            
        user_data = load_data(file, attribute, attribute_value) #Call load data and store to user data
              
        print('Data loaded') 
              
   
   
    elif user_input == 's': #Sorting 
        
        valid_attribute = ['Agility', 'Armor', 'Intelligence', 'Health'] #Valid inputs for sorting 
        valid_order = ['A', 'D'] #valid attributes for order 
        
        value = True 
        while value: #Check if valid input for desired attribute 
            sort_attributes = input("Please enter the attribute you want to use for sorting:\n'Agility', 'Armor', 'Intelligence', 'Health': ")   
            
            if sort_attributes in valid_attribute: #Check if in valid input list 
                value = False
            else:
                print('Invalid input')
        
        value = True
        while value: #Check if valid input for desired attribute 
            order = input("Ascending (A) or Descending (D) order: ")
          
            if order in valid_order:
                value = False 
                
        try: #Try to execute sort data, but if its not able to its becuase the data wasnt loaded first 
                
            sort_data(user_data, order, sort_attributes)
            display_data = input("Data sorted. Do you want to display the data?: ")
            
        except: #Data was not loaded first 
           
            print('Data not loaded')
            continue
      
        if display_data == 'Y':
            print(user_data) #Display data
            
            
    elif user_input == 'c': #Curve fit
        valid_attributes = ["Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Armor", "Weapon"]
        
        
        value = True
        while value: #Check if valid input 
            attribute = input("Please enter the attribute you want to use to find the best fit for health: ")
            
            if attribute in valid_attributes:
                value = False 
            else:
                print('Invalid input')
        try: #see if degree is an int 
            degree = int(input("Please enter the order of the polynomial to be fitted: "))
        except:
            print('Invalid input')
            continue
      
        print(curve_fit(user_data, attribute, degree))
    
    
    elif user_input == 'h': #histogram
        
        value = True
        while value: #check if valid input 
            attribute = input("Please enter the attribute you want to use for plotting: ")
            
            if attribute in valid_attributes:
                value = False
            else:
                print('Invalid input')
                
        histogram(user_data, attribute) #call histogram 
    
    
    elif user_input == 'e': #End program 
        break 
