def almostIncreasing(sequence):

    for i in range(len(sequence)-1):
        if sequence[i+1] <= sequence[i]:
            if (i== 0  or sequence[i+1] > sequence[i-1]):
                sequence.pop(i)
            else:
                sequence.pop(i+1)
            
            for e in range(len(sequence)-1):
                if sequence[e+1] <= sequence[e]:
                    return False
            break
    return True

sequence = [1, 3, 2, 1]
print(almostIncreasing(sequence))


sequence = [1, 3, 2]
print(almostIncreasing(sequence))