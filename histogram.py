# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Adeyemi Oluwafolafunmi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101321952"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-13"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt
import numpy as np


def histogram(data: list[dict], cat: str) -> float:
    """ Returns a histogram of a specified key, given a list of dictionaries.
    Preconditions: type is a key in the dictionary.
    >>> histogram([{'Occupation': 'EB','Armor': 11}, {'Occupation': 'H', 'Armor': 15},{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 12}], "Occupation")
    -1
    >>> histogram([{'Occupation': 'EB','Armor': 15}, {'Occupation': 'H', 'Armor': 10}, {'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 12}], "Armor")
    15
    >>> histogram([{'Occupation': 'EB','Health': 11}, {'Occupation': 'H', 'Health': 14}, {'Occupation': 'EB', 'Health': 13}, {'Occupation': 'H', 'Health': 30}], "Health")
    30
    """
    values = []
    strlist = []
    top = 0
    answer = 0
    for i in data:
        if type(i[cat]) == str:
            values.append(len(i[cat]))
            strlist.append(i[cat])
            answer = -1
        else:
            values.append(i[cat])
            answer = max(values)
            fullrange = np.linspace(0, answer, 20)

    top = max(values)

    fig1 = plt.figure()
    plt.title("Histogram of " + cat)
    plt.xlabel(cat)
    plt.ylabel("y values")
    plt.bar(values, values, 1)
    plt.show()

    return answer

# Do NOT include a main script in your submission

