"""
Practice Task 07: Calculate Sum and Average of Digits Present in a String

Problem Statement:
Write a Python program to run a loop to calculate the sum and average of the 
digits that appear in a string. Ignore all other characters.

Exercise Purpose:
This combines Data Extraction with Arithmetic Operations. It demonstrates 
how to filter relevant data (numbers) out of a "noisy" string (letters and 
symbols) to perform calculations.

Example:
    Input:  str1 = "pynative29@#8496"
    Output: Sum is: 38, Average is 6.33
"""

def calculate_sum_and_average(text):
    """Extracts all digits from the text, calculates their sum and average."""
    total_sum = 0
    count = 0
    
    for char in text:
        if char.isdigit():
            total_sum += int(char)
            count += 1
            
    if count == 0:
        return 0, 0.0
        
    average = total_sum / count
    return total_sum, round(average, 2)


if __name__ == "__main__":
    str1 = "pynative29@#8496"
    print(f"Original String: {str1}")
    
    total_sum, average = calculate_sum_and_average(str1)
    print(f"Sum is: {total_sum} Average is {average}")