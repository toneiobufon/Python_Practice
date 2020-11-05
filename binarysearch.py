
"""
I was bored one day and decided to look at last names in the phonebook for my
area.
I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.
When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."
Example:
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.
*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # Your code here
    #linear pass through a list of names

    #1. need to iterate through the list of names
        #compare two consucutive items
        #second name should be in alphabetical order after the first name
            #if second name is not in order, that is the rotation and we need the index of that name
    #this plan does not take into account that names are in order mostly

    #2. binary search should be considered when searching on sorted data
    #to denote boundaries, we'll have left and right variables
    left = 0
    right= len(surnames)-1

    #loop so long as left < right
    while left < right:
        #get midpoint of the current search space
        mid = ((right-left)//2) + left

        #check midpoint against first element in the search space
        
        if surnames[mid] > surnames[left]:

            #if midpoint > first element, go right
            left = mid

        #else go left
        #when going left, midpoint can't be eliminated since it might be the rotation point
        else:
            right = mid

        #check if element 
        if left+1 == right:
            return right


surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]



print(find_rotation_point(surnames))