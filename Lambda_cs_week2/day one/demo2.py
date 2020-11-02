"""
You are given a non-empty array that represents the digits of a non-negative integer.
Write a function that increments the number by 1.
The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.
You will not receive a leading 0 in your input array (except for the number 0 itself).
Example 1:
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
Example 2:
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
Example 3:
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here
    #given a list of single digit number that together represent a single number
    #increment that number by 1
    #case 1, the right most number is not 9, then increment right most digit by 1
    #case 2, right most digit is a 9
    # change 9 to 0, and add 1 to the left digit, if that number is a 9, the also replace
    #with 0 and add 1 to the left, if all numbers are 9s
    #we might need to add an integer to the most left position

    #1. work with the input in the format that it comes in(in-place)

    #2 transform the input into integers to more easily work with them
    #technically case 2 takes constant extra space since numbers are all represented with a fixed size

    #start iterating from right to left
    for i in range(len(digits)-1, -1, -1):
        #if we realize that no need to iterate(current digit is not a 9), then break the loop
        if digits[i] == 9:
            #change it to 0
            digits[i] = 0
        #otherwise, we continue iterating from right to left as long as need to
        else:
            #increment the digit
            digits[i] += 1
            #since digit is not 9, then break
            return digits

print(plus_one([1,2,9]))