#find the nth smallest number

def nth_smallest(lst, n):
    #given an unsorted array, find the nth smallest
    #return the nth smallest

    #we should sort the list first
    lst.sort()

    #now index to get nth, take into account n-1 for the 0 index
    #this works but we need to check if n is in the range of the list
    if n > len(lst):
        return None
    else: 
        n_small = lst[n-1]
        return n_small


print(nth_smallest([4,6,1,8,9,44,3], 8))
