def do_much(items):

    last_idx = len(items) -1 #getting the length is O(1)


    print(items[last_idx]) #accessing an array via index O(1)
                            #we'll consider printing/console logging O(1)

    middle_idx = len(items)/2 # arithmetic operations O(1)
    idx = 0                    #initializing a variable O(1)

    while idx < middle_idx: #this loop only runs over half the items 
                            # that is 0.5 * n, this is a constant time (n)
        print(items[idx]) # O(1)
        idx = idx+1         #O(1)

    for num in range(2000): # this is a constant O(2000)

        print(num)          #O(1)

""""
to calculate time complexity of the previous example, we only multiply when some logic is nested
when code is stacked sequentially on top of one another, their respective runtimes is added

O(1) + O(1) + O(1) + O(0.5n) + O(2000)
O(0.5n + 2003) --numbers are added
O(n + 2003)--number in front of n is dropped
O(n) -- this is the time complexity of the function
""""



#####################################################################################################

def removeDuplicate(arr):
    differents = {} #initializing variable O(1)

    #in the loop, O(n)* O(1) * O(1)* O(1) = O(n)
  for i in arr:#O(n)
    if i not in differents: #O(1)
        differents[i] = [] #O(1)

    differents[i] += [i] #a couple of things happening here. 1. appending to the end of the list-O(1)
                            #2.accessing the key in the dictionary is O(1)

  return differents.keys() #the `keys` method takes all the keys in the dictionary 
                            #and returns them all as a list, that is O(n)

"""
the time complexity here is O(n)+ O(n)= O(2*n) = O(n)
"""

#######################################################################################################