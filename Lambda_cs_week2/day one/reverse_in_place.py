#how to implement a reverse array in place

def reverse(arr):
    #this does not work because slicing creates a copy of the input array
    
    #return arr[::-1]
    left = 0
    right = len(arr)-1

    #how do we iterate
    # iterate so long as left < right
    while left < right:
        #if there is an odd element in the input arr
        # we hace the case where left and right land on the middle element
        # swap the elements they are pointing at
        # this does use an extra `temp` variable under the hood
        arr[left], arr[right]  = arr[right], arr[left]
        #increment the left pointer
        left +=1

        #decrement the right pointer
        right -= 1

    return arr

print(reverse([4,1,6,3,33,22]))