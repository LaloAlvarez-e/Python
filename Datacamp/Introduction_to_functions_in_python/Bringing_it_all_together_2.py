#!C:\git\Python\Datacamp\Introduction_to_functions_in_python\venv\Scripts\python.exe

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:20:28 2019

"""

import os
import pandas as pd


def read_file_raw(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file 'tweets.csv' was not found at {file_path}")
        print("Please ensure the file exists in the same directory as this script.")
    except PermissionError:
        print(f"Error: Permission denied to read {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define count_entries()
def count_entries(file_path, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return (langs_count)

def count_entries_performance(file_path, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    # Read the CSV file into a DataFrame
    # Import Twitter data as DataFrame: df
    lang_counts = None
    df = pd.read_csv(file_path)
    if col_name in df.columns:
        lang_counts = df[col_name].value_counts()
    return lang_counts

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory: {script_dir}")
    file_path = os.path.join(script_dir, 'tweets.csv')
    print(f"Constructed file path: {file_path}")

    # Read and print CSV file
    try:
        langs_count = count_entries(file_path, 'lang')
        # Print the populated dictionary
        print(langs_count)

        lang_counts = count_entries_performance(file_path, 'lang')
        print(lang_counts)
    except FileNotFoundError:
        print(f"Error: The file 'tweets.csv' was not found at {file_path}")
        print("Please ensure the file exists in the same directory as this script.")
    except PermissionError:
        print(f"Error: Permission denied to read {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
