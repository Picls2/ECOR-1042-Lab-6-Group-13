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
from load_data import load_data, calculate_health
from sort import sort

while True: 
    valid_attributes = ["Occupation", "Strength", "Luck", "Weapon", "All"]
    
    restart = True 
    if restart:
        restart = False #Will be set back to true of user makes error
    
        print("The available commands are: \nLoad Data)\nS)ort Data\nC)urve fit\nH)istogram\nE)exit\n") #Display the user interface options 
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
            
        user_data = calculate_health(load_data(file, (attribute, attribute_value))) #Call load data and calculate_health and store to user data
              
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
                
            sort(user_data, order, sort_attributes)
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
        valid_attributes = ["Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Armor", "Weapon"]
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
