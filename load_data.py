# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Nicholas Dorscht, Evan Mallot, Andy Muka, Oluwafolafunmi Adeyemi"

# Update "" with your team (e.g. T102)
__team__ = "T-013"


#==========================================#
# Place your character_occupation_list function after this line
def character_occupation_list(character_file: str, occupation: str) -> list[dict]:
    """
    Takes a file path and a type of occupation, and then returns a list of dictionaries containing 
    all of the players stats that are part of that occupation. It does not return the occupation.
    Preconditions: character_file must be a valid file path, and occupation must be a string.
    >>> character_occupation_list('./characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}] 
    
    >>> character_occupation_list('./characters-mat.csv', 'M')
    [{'Strength': 14, 'Agility': 7, 'Stamina': 13, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Dagger'}]
    
    >>> character_occupation_list('./characters-mat.csv', 'VF')
    [{'Strength': 12, 'Agility': 12, 'Stamina': 10, 'Personality': 12, 'Intelligence': 8, 'Luck': 0.78, 'Armor': 11, 'Weapon': 'Spear'}]
    """

    characters = []
    first_line = True
    file = open(character_file, 'r')

    for line in file:
        line = line.strip().split(",")
        if first_line:
            first_line = False
            continue
        elif line[0] == occupation:
            player = {}
            player["Strength"] = int(line[1])
            player["Agility"] = int(line[2])
            player["Stamina"] = int(line[3])
            player["Personality"] = int(line[4])
            player["Intelligence"] = int(line[5])
            player["Luck"] = float(line[6])
            player["Armor"] = int(line[7])
            player["Weapon"] = line[8]

            characters.append(player)
    file.close()
    return characters

#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(file_name: str, strength_range: tuple) -> list[dict]:
    character_list = []
    character = {}
    table_header = []
    in_file = open(file_name, 'r')
    first_line = True

    for line in in_file:
        line = line.strip().split(',')

        if first_line:
            first_line = False
            table_header = line

        else:
            if int(line[1]) <= strength_range[1] and int(line[1]) >= strength_range[0]:
                character = {}
                character[table_header[0]] = line[0]
                character[table_header[2]] = int(line[2])
                character[table_header[3]] = int(line[3])
                character[table_header[4]] = int(line[4])
                character[table_header[5]] = int(line[5])
                character[table_header[6]] = float(line[6])
                character[table_header[7]] = int(line[7])
                character[table_header[8]] = line[8]
                character_list.append(character)
    in_file.close()

    return character_list

#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file_name: str, luck: float) -> list[dict]:
    """
    >>> character_luck_list('./characters-mat.csv', 0.5)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'WA', 'Strength': 12, 'Agility': 9, 'Stamina': 6, 'Personality': 14, 'Intelligence': 10, 'Armor': 10, 'Weapon': 'Spear'}]
    >>> character_luck_list('./characters-mat.csv', 0.2)
    [{'Occupation': 'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14, 'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    >>> character_luck_list('./characters-mat.csv', 0.1)
    []
    """

    in_file = open(file_name, "r")
    first_line = True
    character_list = []
    table_header = []

    for line in in_file:

        line = line.strip()

        line = line.split(',')

        if first_line:
            first_line = False
            table_header = line

        elif float(line[6]) < luck:
            character = {}
            character[table_header[0]] = line[0]
            character[table_header[1]] = int(line[1])
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[7]] = int(line[7])
            character[table_header[8]] = line[8]

            character_list.append(character)

    in_file.close()
    return character_list


#==========================================#
# Place your character_weapon_list function after this line
def character_weapon_list(file_name: str, weapon: str) -> list[dict]:
    """ Returns the list of characters stored as a dictionary whose weapon is provided as the input parameters.

    Precondition: file_name has the following columns
    ["Occupation", "Strength","Agility", "Stamina",
        "Personality", "Intelligence", "Luck", "Armor", "Weapon"]

    >>> character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …
    ]

    >>> character_weapon_list ('characters-mat.csv', 'aaa')
    []
    """

    file = open(file_name, 'r')

    first_line = True
    result = []

    for line in file:

        line = line.strip()
        line = line.split(',')

        if first_line:
            first_line = False
            header = line

        else:
            records = {}
            records[header[0]] = line[0]
            records[header[1]] = int(line[1])
            records[header[2]] = int(line[2])
            records[header[3]] = int(line[3])
            records[header[4]] = int(line[4])
            records[header[5]] = int(line[5])
            records[header[6]] = float(line[6])
            records[header[7]] = int(line[7])

            if line[8] == weapon:
                result.append(records)
    file.close()
    return result

#==========================================#
# Place your load_data function after this line


def load_data(file_name: str, attribute_tuple: tuple) -> list[dict]:
    """
    Takes a file name and a choice of attribute and returns all of the characters that contain that attribute with the
    given value of the attribute. If the passed attribute is "all", then a list of all the characters is returned.
    Preconditions: file_name must be a valid file path, and attribute_tuple must be a tupple with two values, the first 
    one being the attribute, and the second being the value.
    >>> load_data('./characters-mat.csv', ('strength', (3, 8)))
    [{'Occupation': 'AT', 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9, 'Weapon': 'Dagger'}, ...  {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}]
    >>> load_data('./characters-mat.csv', ('weapon', 'Dagger'))
    [{'Occupation': 'AT', 'Strength': 7, 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9} ... {'Occupation': 'AT', 'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10}]
    >>> load_data('./characters-mat.csv', ('h', 'Dagger'))
    Enter a valid attribute.
    """

    attribute = attribute_tuple[0].lower()
    if attribute == 'occupation':
        return character_occupation_list(file_name, attribute_tuple[1])
    elif attribute == 'strength':
        return character_strength_list(file_name, attribute_tuple[1])
    elif attribute == 'luck':
        return character_luck_list(file_name, attribute_tuple[1])
    elif attribute == 'weapon':
        return character_weapon_list(file_name, attribute_tuple[1])
    elif attribute == 'all':
        characters = []
        first_line = True
        line_headers = []
        file = open(file_name, 'r')

        for line in file:
            line = line.strip().split(",")
            if first_line:
                first_line = False
                line_headers = line
            else:
                player = {}
                player[line_headers[0]] = line[0]
                player[line_headers[1]] = int(line[1])
                player[line_headers[2]] = int(line[2])
                player[line_headers[3]] = int(line[3])
                player[line_headers[4]] = int(line[4])
                player[line_headers[5]] = int(line[5])
                player[line_headers[6]] = float(line[6])
                player[line_headers[7]] = int(line[7])
                player[line_headers[8]] = line[8]

                characters.append(player)
        file.close()
        return characters
    else:
        print("Invalid Value")
        return []
    return
#==========================================#
# Place your calculate_health function after this line


def calculate_health(character_list: list[dict]) -> list[dict]:
    """
    Takes a list of characters and returns a new list containing the same characters but with updated dictionaries with their
    calcualted health.
    Preconditions: Assumes that all character attributes are present for the calcuation, however "Occupation" and "Weapon"
    are not necessary.
    >>> calculate_health(load_data('./characters-mat.csv', ("Occupation", "AT")))
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff', 'Health': 78.88}, ... {'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff', 'Health': 67.12}]
    >>> calculate_health(load_data('./characters-mat.csv', ("Weapon", "Dagger")))
    [{'Occupation': 'AT', 'Strength': 7, 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9, 'Health': 110.18}, ... {'Occupation': 'AT', 'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Health': 92.0}]
    >>> calculate_health(load_data('./characters-mat.csv', ("all", "0")))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff', 'Health': 78.88}, ... {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff', 'Health': 67.12}]
    """
    new_list = []

    for character in character_list:
        health = (character["Strength"] + character["Agility"] + character["Stamina"] + character["Personality"] +
                  character["Intelligence"]) + (character["Armor"] ** 2 * character["Luck"])

        character["Health"] = health

        new_list.append(character)

    return new_list
# Do NOT include a main script in your submission