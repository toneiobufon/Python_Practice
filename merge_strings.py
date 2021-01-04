"""
merge two strings, by comparing every character and insert smallest character first
example:
s1 = 'super'
s2 = 'tower'

merged(s1,s2) = 'stouperwer'

"""

def merged_strings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    merged = []

    for i in range(len(s1)):  
        if s1[i] < s2[i]:
            merged.append(s1[i])
            i+=1
                 
        else:
            merged.append(s2[i])
            i+=1
                
    print(merged)
    new = ''.join(merged)

    return new 

s1 = 'super'
s2 = 'tower' 
print(merged_strings(s1,s2))