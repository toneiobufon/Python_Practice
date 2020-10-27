"""
Challenge #1:
Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []
Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    #your code here
    #if n is longer than the length of the list, return invalid
    if n > len(a):
        return "invalid"
    #if n == 0 return an empty list []
    elif n == 0:
        return []
    else:
        return a[n:]
a = [4, 3, 9, 9, 7, 6]
b = [1, 2, 3, 4, 5]
c= [1, 2, 3, 4, 5]
print(last(a,3))
print(last(b,6))
print(last(c,0))