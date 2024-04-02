# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nicholas Dorscht"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298132"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-013"

#==========================================#

import numpy as np
import matplotlib.pyplot as plt
# Place your histogram function after this line
def histogram(characters: list[dict], atr: str) -> float :
    """
    """
    
    graph_data = {}
    # Check attribute type
    if isinstance(characters[0][atr], str) :
        
        # Find amount in each type
        
        for character in characters :
            if character[atr] in graph_data :
                graph_data[character[atr]] += 1
            else :
                graph_data[character[atr]] = 1
                
        code = -1
    elif isinstance(characters[0][atr], int) or isinstance(characters[0][atr], float) :
        
        for character in characters :
            if character[atr] in graph_data :
                graph_data[character[atr]] += 1
            else :
                graph_data[character[atr]] = 1
        
        # Make 20 equal bins
        full_x_range = np.linspace(0, max(list(graph_data.keys())), 20)
        
        for num in full_x_range :
            graph_data.setdefault(round(num, 2), 0)
        
        code = max(list(graph_data.keys()))
        
    
    # Create chart
    
    fig = plt.figure()
    plt.title(f"Number of Characters With Each {atr}")
    plt.xlabel(atr)
    plt.ylabel("# of Characters")
    plt.bar(list(graph_data.keys()), list(graph_data.values()), 1)
    plt.show()

    return code
# Do NOT include a main script in your submission

