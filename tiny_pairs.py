"""
concatenate ints from two arrays, and check if the concatenated pairs of 
ints are less than the given number.
ex: 
a = [1,2,3]
b = [1,2,3]
k= 31
11,22
result should be 2
"""

def tiny_pairs(a,b,k):

    count = 0

    for i in range(0, len(a)):
        
        s = int(str(a[i]) + str(b[i])) 
            
        print(s)
        if s < k:
            count +=1
    
    return count


a= [1,2,3,4]
b= [1,2,3,4]
k = 51

print(tiny_pairs(a,b,k))