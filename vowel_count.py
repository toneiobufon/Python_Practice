"""
Challenge #6:
Return the number (count) of vowels in the given string.
We will consider `a, e, i, o, u as vowels for this challenge (but not y).
The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    # count number of vowels
    #keep a counter to keep track of vowels
    num_vowels = 0
    #list to compare each char
    vowels = 'aeiou'
    #we need to iterate the string to inspect every character to check for a vowel
    for char in input_str:

    #if i is a vowel, then increment counter
        if char in vowels:
            num_vowels += 1
    #return counter
    return num_vowels

print(get_count("aeiouauau"))