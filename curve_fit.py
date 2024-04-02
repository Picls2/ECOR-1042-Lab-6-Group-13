# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nicholas Dorscht"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298132"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-013"

#==========================================#
import numpy as np

# Place your curve_fit function after this line
def curve_fit(characters: list[dict], compared_trait: str, deg: int) -> str :
    """
    Takes a list of characters, a trait that is to be compared between them and a degree of a polynomial
    and returns a polynomial that represents a curve that is fitted to the characters health to their 
    compared trait.
    Preconditions: Both "Health" and the compared trait must be present in all character dictionaries
    >>> curve_fit([{"Agility": 1,"Health": 44,"Armor": 1},{"Health": 56,"Agility": 2,"Armor": 1},{"Health": 64,"Agility": 1,"Armor": 3},{"Health": 67,"Agility": 3,"Armor": 2},{"Health": 74,"Agility": 3,"Armor": 3},{"Health": 88,"Agility": 4,"Armor": 4}], "Armor", 3)
    5.333333333333254x^3-39.49999999999956x^2+98.1666666666662x-13.999999999999858
    >>> curve_fit([{"Agility": 1,"Health": 44,"Armor": 1},{"Health": 56,"Agility": 2,"Armor": 1},{"Health": 64,"Agility": 1,"Armor": 3},{"Health": 67,"Agility": 3,"Armor": 2},{"Health": 74,"Agility": 3,"Armor": 3},{"Health": 88,"Agility": 4,"Armor": 4}], "Agility", 4)
    -0.3086067622362218x^4+1.5027342890288968x^3+4.948763321732127x^2-18.7363285548553x+66.59343770633049
    >>> curve_fit([{"Agility": 1,"Health": 44,"Armor": 1},{"Health": 56,"Agility": 2,"Armor": 1},{"Health": 64,"Agility": 1,"Armor": 3},{"Health": 67,"Agility": 3,"Armor": 2},{"Health": 74,"Agility": 3,"Armor": 3},{"Health": 88,"Agility": 4,"Armor": 4}], "Agility", 3)
    -1.583333333333329x^3+15.750000000000025x^2-34.16666666666687x+74.00000000000011
    """
    trait_values = {}
    
    # Map health values to trait values
    for character in characters :
        if character[compared_trait] in trait_values :
            trait_values[character[compared_trait]].append(character["Health"])
        else :
            trait_values[character[compared_trait]] = [character["Health"]]
    
    # Calculate average health for each trait value
    for trait, health in trait_values.items() :
        trait_values[trait] = sum(health) / len(health)
    
    # Find coefficients
    
    if deg > len(trait_values) - 1:
        coef = np.polyfit(list(trait_values.keys()), list(trait_values.values()), len(trait_values) - 1)
    else :
        coef = np.polyfit(list(trait_values.keys()), list(trait_values.values()), deg)
        
    #Concatenate coefficients into string
    
    poly = f"{coef[0]}x^{len(coef) - 1}"
    
    #Check for coefficient's sign
    for i in range(1, len(coef)) :
        if coef[i] < 0 :
            sign = ''
        else :
            sign = '+'
        
        # Check for position in polynomial
        if i == len(coef) - 2:
            poly += f'{sign}{coef[i]}x'
        elif i == len(coef) - 1 :
            poly += f'{sign}{coef[i]}'
        else : 
            poly += f'{sign}{coef[i]}x^{len(coef) - i - 1}'
        
    return poly
# Do NOT include a main script in your submission