"""
create a function that takes two strings s1 and s2, and returns the lexicographically
smallest result that can be obtained by placing the symbols of s2 between the symbols
of s1 in such a way that maintains the relative order of the characters in each 
string

For example, if s1 = 'super' and s2 = 'tower,' the result should be 
merge(s1,s2) = 'stouperwer'
"""

def mergeString(s1,s2):
    s1= list(s1)
    s2= list(s2)
    
    new = []

    for i in range(len(s1)):
        
        if str(s1[i]) < str(s2[i]):
            new.append(str(s1[i]))
               
        else:
            new.append(str(s2[i]))
                

    joined = ''.join(new)

    return joined


s1 = "super"
s2 = "tower"
print(mergeString(s1,s2))