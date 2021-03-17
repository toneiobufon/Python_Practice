# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inArray):
    sor = sorted(inArray, key=len)

    nw = []

    for i in range(len(inArray)):
        if len(inArray[i]) == len(sor[-1]):
            nw.append(inArray[i])
    
    return nw

inArray = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(inArray))