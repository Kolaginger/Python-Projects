"""
Practice Task 04: Remove All Characters Except Integers (Digit Extraction)

Problem Statement:
Write a Python program to extract only the numeric digits from a mixed string 
and combine them into a single string. This is a core data extraction technique 
used in web scraping and OCR text processing to strip away noise like currency, 
labels, and spaces to obtain raw numerical data.

Example:
    Input:  str1 = "I am 25 years and 10 months old"
    Output: "2510"
"""

def extract_digits(text):
    """Extracts all numeric digits from the text and joins them into a single string."""
    keep_digits = []
    for char in text:
        if char.isdigit():
            keep_digits.append(char)
    return "".join(keep_digits)


if __name__ == "__main__":
    str1 = "I am 25 years and 10 months old"
    print(f"Original String: {str1}")
    
    result = extract_digits(str1)
    print(f"Extracted Digits: {result}")