"""
Practice Task 02: Palindrome Checker

Problem Statement:
Write a Python function that checks whether a given string reads the same 
forwards and backwards, ignoring case and spaces.

Example:
    Input:  "Racecar"
    Output: True
"""

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample = "Racecar"
    print(f"Input: {sample} | Is Palindrome: {is_palindrome(sample)}")