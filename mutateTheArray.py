"""
given an integer 'n' and an array 'a' of length 'n, mutate 'a' in the 
following sequence. 

array 'a' mutates into a new array b of length 'n'

for each i from o to n-1, b[i] = a[i-1] + a[i] + a[i+1]
if some element in the sum a[i-1] +a[i+1] does not exist, it should
be set to 0. For example, b[0] should be equal to 0 + a[0] +a[1].

for n=5 and a= [4,0,1,-2,3], the output should be b = [4,5,-1,2,1]

b[0] = 0 + a[0] + a[1] = 0 +4 +0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = -1 + 3 + 0 = 1

"""

def mutateTheArray(n,a):

    b = []

    for i in range(0, n-1):
        
        if i == 0:
            i = a[0] +a[1]
            b.append(i)
        else:
            i = a[i-1] +a[i] + a[i+1]
            b.append(i)
    
    return b 
        




n = 5
a = [4,0,1,-2,3]
print(mutateTheArray(n,a))

