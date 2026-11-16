"""
Practice Task 06: Remove Empty Strings and None Values from a List

Problem Statement:
Write a Python program to remove any empty strings (`""`) or `None` values 
from a given list of strings.

Exercise Purpose:
This introduces Data Cleaning. Real-world datasets often have missing or 
empty values. Learning to filter lists is essential to prevent your program 
from crashing when processing empty data points.

Example:
    Input:  str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    Output: ['Emma', 'Jon', 'Kelly', 'Eric']
"""

def remove_empty_elements(data_list):
    """Filters out empty strings and None values from the provided list."""
    # Keep elements that are not None and not an empty string
    return [item for item in data_list if item]


if __name__ == "__main__":
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    print(f"Original List: {str_list}")
    
    cleaned_list = remove_empty_elements(str_list)
    print(f"Cleaned List: {cleaned_list}")