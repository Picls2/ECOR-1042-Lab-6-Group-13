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
from load_data import load_data, calculate_health
from sort import sort

def run_commands(commands: list) -> None :
    for command in commands :
        if command[0] == 'l':
            character_data = calculate_health(load_data(command[1], (command[2], command[3])))
            print("Data Loaded")
            
        elif command[0] == 's' :
            sort(character_data, command[2], command[1])
            
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