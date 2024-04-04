# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Nicholas Dorscht, Evan Mallot, Andy Muka, Oluwafolafunmi Adeyemi"

# Update "" with your team (e.g. T102)
__team__ = "T-013"

#==========================================#
# Place your sort_characters_agility_bubble function after this line
def sort_characters_agility_bubble(character_list: list, order: str) -> list:
    """Take a list of characters and an order of arrangement. Sort the list based
    on give parameter of 'A' for ascending or 'D'for descending. Sort through the 
    'Agiligty attribute within a dictionary and reorder based on parameter. Return a 
    reordered list or if 'Agility' is not in Diction then return origonal list. 
    
    Pre-condtions: character_list == type list, order == type str. order == 'A' or 
    'D'. 
    
    >>>sort_characters_agility_bubble([{'Occupation': 'EB',
    'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], 'A')
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]

    >>>sort_characters_agility_bubble([{'Occupation':'EB'}, {'Occupation': 'M'}], 'A')
    "Agility" key is not present
    [{'Occupation':'EB'}, {'Occupation': 'M'}]
    
    >>>sort_characters_agility_bubble([{'Strength': 13, 'Agility': 2}, {'Agility': 9, 'Stamina': 8}], 'D')
    [{'Agility': 9, 'Stamina': 8}, {'Strength': 13, 'Agility': 2}]
    
    
    """
    origonal_character_list = character_list 
    
    switch = True
    
    for i in range(len(character_list)):
        if 'Agility' not in character_list[i]: 
            print('Agility key is not present')
            return character_list
        
    
    
    if order == 'A':
        while switch:
            switch = False
            for i in range(len(character_list) - 1):
                
                
                    if character_list[i]['Agility'] > character_list[(i + 1)]['Agility']:
                        
                        
                        reorder = character_list[i]
                        character_list[i] = character_list[i + 1]
                        character_list[i + 1] = reorder
                        switch = True
                            
    if order == 'D':
        
        while switch:
            switch = False
            for i in range(len(character_list) - 1):
                    if character_list[i]['Agility'] < character_list[(i + 1)]['Agility']:
                        
                        reorder = character_list[i]
                        character_list[i] = character_list[i + 1]
                        character_list[i + 1] = reorder
                        switch = True
                               
    return character_list
#==========================================#
# Place your sort_characters_intelligence_selection function after this line
def sort_characters_intelligence_selection(dictionaries: list, order: str) -> list:
    """Return a sorted dictionary by the "Intelligence" key 

    preconcition: "order" is either "a" or "'d"

    >>>sort_characters_intelligence_selection([{'Occupation': 'EB',
    'Intelligence': 9}, {'Occupation': 'H',
    }], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H'}]
    sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 9}, {'Occupation': 'H','Intelligence': 12}], "D")
    >>>sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 9}, {'Occupation': 'H','Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]
    >>>sort_characters_intelligence_selection([{'Occupation': 'EB'}, {'Occupation': 'H'}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'H'}]
    """
    if not dictionaries:
        return dictionaries
    for i in dictionaries:
        if "Intelligence" not in i:
            print("\"Intelligence\" key is not present")
            return dictionaries

    if order == "a" or order == "A":
        for i in range(len(dictionaries)):
            min_idx = i
            for j in range(i + 1, len(dictionaries)):
                if dictionaries[min_idx].get("Intelligence") > dictionaries[j].get("Intelligence"):
                    min_idx = j
            dictionaries[i], dictionaries[min_idx] = dictionaries[min_idx], dictionaries[i]

        return dictionaries

    elif order == "d" or order == "D":
        for i in range(len(dictionaries)):
            max_idx = i
            for j in range(i + 1, len(dictionaries)):
                if dictionaries[max_idx].get("Intelligence") < dictionaries[j].get("Intelligence"):
                    max_idx = j

            dictionaries[i], dictionaries[max_idx] = dictionaries[max_idx], dictionaries[i]

        return dictionaries

#==========================================#
# Place your sort_characters_health_insertion function after this line
def sort_characters_health_insertion(characters: list[dict], order: str) -> list[dict] :
    """    Sorts a list of characters based on their health value, passing A into the order argument
    sorts them into ascending order and D sorts them into descending order. If the "Health" value 
    is not present in any of the character dictionaries then the original list is returned and an error message is printed.
    >>> sort_characters_health_insertion([{"Health" : 45}, {"Health" : 435}, {"Health" : 9}, {"Health" : 23}], "D")
    [{'Health': 435}, {'Health': 45}, {'Health': 23}, {'Health': 9}]
    >>> sort_characters_health_insertion([{"Health" : 45}, {"Health" : 435}, {"Health" : 9}, {"Health" : 23}], "A")
    [{'Health': 9}, {'Health': 23}, {'Health': 45}, {'Health': 435}]
    >>> sort_characters_health_insertion([{"Health" : 45}, {"asjdfhds" : 435}, {"Health" : 9}, {"Health" : 23}], "A")
    The "Health" key is not in the character dictionary
    [{'Health': 45}, {'asjdfhds': 435}, {'Health': 9}, {'Health': 23}]
    """
    original = characters
    
    if order == "A" :
        for i in range(1, len(characters)) :
            key = characters[i]
            
            j = i - 1
            
            if not("Health" in characters[i]) :
                print("The \"Health\" key is not in the character dictionary")
                return original
            
            while j >= 0 and key["Health"] < characters[j]["Health"] :
                characters[j + 1] = characters[j]
                j -= 1
                
            characters[j + 1] = key
        
        return characters
    elif order == "D" :
        for i in range(1, len(characters)) :
            key = characters[i]
            
            if not("Health" in characters[i]) :
                print("The \"Health\" key is not in the character dictionary")
                return original
            
            j = i - 1
            while j >= 0 and key["Health"] > characters[j]["Health"] :
                characters[j + 1] = characters[j]
                j -= 1
                
            characters[j + 1] = key
        return characters

#==========================================#
# Place your sort_characters_armor_bubble function after this line
def sort_characters_armor_bubble(data: list[dict], order: str) -> list[dict]:
    """ Sorts a list of dictionaries by the armor value.
    Precondition: must contain Armor key and order = A or D.
    >>>sort_characters_armor_bubble([{'Occupation': 'EB','Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "D")
    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

    >>>sort_characters_armor_bubble([{'Occupation': 'EB'},{'Occupation': 'M'}], "D")
    "Armor" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """
    for i in range(len(data)):
        num = 0
        text = '"Armor key" is not present'
        if "Armor" not in data[i]:
            num = 1
            print(text * num)
            return data

    swap = True
    if order == "A":
        while swap:
            swap = False
            for i in range(len(data) - 1):
                if data[i]["Armor"] > data[i + 1]["Armor"]:
                    larger = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = larger
                    swap = True
    if order == "D":
        while swap:
            swap = False
            for i in range(len(data) - 1):
                if data[i]["Armor"] < data[i + 1]["Armor"]:
                    larger = data[i + 1]
                    data[i + 1] = data[i]
                    data[i] = larger
                    swap = True

    return data

#==========================================#
# Place your sort function after this line
def sort(characters: list[dict], order: str, attribute: str) -> list[dict] :
    """
    Sorts the list of characters based on the given attribute, in ascending order if "order" 
    is passed as "A" and descending order if it is given as "D". If an attribute that does not exist
    is passed then an error message is given and the original list is returned.
    >>> sort([{"Health": 33, "Agility": 2, "Armor": 23, "Intelligence": 3}, {"Health": 353, "Agility": 6, "Armor": 223, "Intelligence": 73},{"Health": 343, "Agility": 752, "Armor": 223, "Intelligence": 13},{"Health": 133, "Agility": 23, "Armor": 232, "Intelligence": 7}], "A", "Health")
    [{'Health': 33, 'Agility': 2, 'Armor': 23, 'Intelligence': 3}, {'Health': 133, 'Agility': 23, 'Armor': 232, 'Intelligence': 7}, {'Health': 343, 'Agility': 752, 'Armor': 223, 'Intelligence': 13}, {'Health': 353, 'Agility': 6, 'Armor': 223, 'Intelligence': 73}]
    >>> sort([{"Health": 33, "Agility": 2, "Armor": 23, "Intelligence": 3}, {"Health": 353, "Agility": 6, "Armor": 223, "Intelligence": 73},{"Health": 343, "Agility": 752, "Armor": 223, "Intelligence": 13},{"Health": 133, "Agility": 23, "Armor": 232, "Intelligence": 7}], "D", "Armor"))
    [{'Health': 133, 'Agility': 23, 'Armor': 232, 'Intelligence': 7}, {'Health': 353, 'Agility': 6, 'Armor': 223, 'Intelligence': 73}, {'Health': 343, 'Agility': 752, 'Armor': 223, 'Intelligence': 13}, {'Health': 33, 'Agility': 2, 'Armor': 23, 'Intelligence': 3}]
    >>> sort([{"Health": 33, "Agility": 2, "Armor": 23, "Intelligence": 3}, {"Health": 353, "Agility": 6, "Armor": 223, "Intelligence": 73},{"Health": 343, "Agility": 752, "Armor": 223, "Intelligence": 13},{"Health": 133, "Agility": 23, "Armor": 232, "Intelligence": 7}], "D", "Agility")
    [{'Health': 343, 'Agility': 752, 'Armor': 223, 'Intelligence': 13}, {'Health': 133, 'Agility': 23, 'Armor': 232, 'Intelligence': 7}, {'Health': 353, 'Agility': 6, 'Armor': 223, 'Intelligence': 73}, {'Health': 33, 'Agility': 2, 'Armor': 23, 'Intelligence': 3}]
    """
    
    if attribute == "Agility" :
        return sort_characters_agility_bubble(characters, order)
    elif attribute == "Intelligence" :
        return sort_characters_intelligence_selection(characters, order)
    elif attribute == "Health" :
        return sort_characters_health_insertion(characters, order)
    elif attribute == "Armor" :
        return sort_characters_armor_bubble(characters, order)
    else :
        print(f"Cannot be sorted by {attribute}")
        return characters
# Do NOT include a main script in your submission