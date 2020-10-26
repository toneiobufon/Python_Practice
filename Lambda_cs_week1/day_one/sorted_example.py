#create a function that sorts a list of strings by length in ascending order
def sort_by_length(lst):
    #sort items, shorter items first
    #the .sort method on lists in python sorts in place


    new =sorted(lst)
    return new

print(sort_by_length(['name', 'nam', 'named']))