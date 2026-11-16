"""
Practice Task 05: Remove Special Symbols and Punctuation

Problem Statement:
Write a Python program to remove all special symbols and punctuation from a given string.
This is a core staple of Natural Language Processing (NLP). Before analyzing text like 
sentiment analysis, you must remove "noise" such as symbols and punctuation so the computer 
can focus strictly on the words.

Example:
    Input:  str1 = "/*Jon is @developer & musician! !"
    Output: "Jon is developer musician"
"""

def remove_from_string(text):
    """Removes all special punctuation symbols while preserving alphanumeric characters and spaces."""
    cleaned_chars = []
    for char in text:
        # Keep character if it is alphanumeric (letters/numbers) or a whitespace
        if char.isalnum() or char.isspace():
            cleaned_chars.append(char)
    return "".join(cleaned_chars)


if __name__ == "__main__":
    str1 = "/*Jon is @developer & musician! !"
    print(f"Original String: {str1}")
    
    result = remove_from_string(str1)
    print(f"Cleaned Output: {result}")