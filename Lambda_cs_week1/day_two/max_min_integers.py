"""
Challenge #10:
Given a string of space separated integers, write a function that returns the
maximum and minimum integers.
Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"
Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    #given a string of numbers, we need to figure out the min and max
    #we have functions max and min  that find max and min for us, but only work wot
    
    #we can split the input string on spaces
    str_digits = input_str.split(' ')
    int_digits = []

    #transform each str_digit into a number
    #we can use the `int` function for that
    for str_digit in str_digits:
        int_digit = int(str_digit)
        int_digits.append(int_digit)


    #onvce we have a list of numbers, we can then use max and min functions
    ma = max(int_digits)
    mi = min(int_digits)

    #use an f-string interpolation to return desired version

    return f"{ma} {mi}"

print(max_and_min("1 2 3 4 5"))
