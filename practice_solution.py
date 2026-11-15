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

#Given input
str1 = "google"

#Call the function and print the result
result = remove_duplicate_char(str1)
print(result)