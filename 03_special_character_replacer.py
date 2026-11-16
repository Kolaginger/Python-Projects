"""
Practice Task 03: Special Character Sanitization / Replacer

Problem Statement:
Write a Python program to replace every special symbol (punctuation) in a 
string with a specific target character, such as '#'. This is vital for 
data sanitization before sending text to systems or databases that cannot 
handle special symbols.

Example:
    Input:  str1 = "/*Jon is @developer & musician! !"
    Output: "##Jon is #developer # musician##"
"""

import string

def sanitize_string(text, replacement_char="#"):
    """Replaces all punctuation symbols in the text with the replacement_char."""
    for char in string.punctuation:
        text = text.replace(char, replacement_char)
    return text


if __name__ == "__main__":
    str1 = "/*Jon is @developer & musician! !"
    print(f"Original String: {str1}")
    
    sanitized = sanitize_string(str1, "#")
    print(f"Sanitized Output: {sanitized}")