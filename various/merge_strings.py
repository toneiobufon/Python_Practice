"""
merge two strings, by comparing every character and insert smallest character first
example:
s1 = 'super'
s2 = 'tower'

merged(s1,s2) = 'stouperwer'

"""

def merged_strings(s1, s2):
    # s1 = list(s1)
    # s2 = list(s2)

    # merged = []

                
                
    # print(merged)
    # new = ''.join(merged)

    # return new 

    counts = {}
    for char in s1:
        if char in counts:
            counts[char] += 1
        else: 
            counts[char] = 1
            
    s1dict = counts
    #reset
    counts = {}
    
    for char in s2:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    s2dict = counts
    p1, p2 = 0, 0
    output = []
    print(s1dict, s2dict)
    
    while p1 < len(s1) and p2 < len(s2):
        char1, char2 = s1[p1], s2[p2]
        count1, count2 = s1dict[char1], s2dict[char2]
        if count1 == count2:
            if char1 < char2:
                output.append(char1)
                p1 += 1
            else:
                output.append(char2)
                p2 += 1
        elif count1 < count2:
            output.append(char1)
            p1 += 1
        else:
            output.append(char2)
            p2 += 1
    while p1 < len(s1):
        output.append(s1[p1])
        p1 += 1
    while p2 < len(s2):
        output.append(s2[p2])
        p2 += 1
    return "".join(output)

s1 = 'super'
s2 = 'tower' 
print(merged_strings(s1,s2))

