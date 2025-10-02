#!C:\git\Python\Datacamp\Introduction_to_functions_in_python\venv\Scripts\python.exe

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:20:28 2019

"""
# Define shout with parameters word1 and word2
def shout_all(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    new_shout = (shout1 , shout2)
    # Replace print with return
    return (new_shout)


def main():
    # Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
    yell1, yell2 = shout_all('congratulations', 'you')


    # Print yell1 and yell2
    print(yell1)
    print(yell2)


if __name__ == "__main__":
    main()

# A function that returns multiple values
def f():
    return 1, 2, 3