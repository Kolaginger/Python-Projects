"""
Practice Task 01: Remove Duplicate Characters from a String

Problem Statement:
Write a Python function that takes a string as input and removes all 
duplicate characters while preserving the original order of first appearance.

Example:
    Input:  "google"
    Output: "gole"
"""

def remove_duplicate_char(text):
  #Create empty lists for seen and result
  seen_list = []
  results = []

  #Loop through every word
  for char in text:
    if char not in seen_list:
      seen_list.append(char)
      results.append(char)

  #Join words back into a single sentence
  return "".join(results)

if __name__ == "__main__":
    sample_text = "google"
    result = remove_duplicate_char(sample_text)
    print(f"Original: {sample_text} | Cleaned: {result}")
