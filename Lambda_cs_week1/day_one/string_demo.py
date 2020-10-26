def string_int(txt):
    #check to make sure txt makes sense as an integer
    # to check, we use `isnumeric` function 

    #if txt is a valid number
    if txt.isnumeric() is True:
        #using the int function to convert the txt into an integer
        return int(txt)
    
    #if txt is not numeric/valid number
    else:
        #we get an error indicating that txt is not a valid number
        #we will use f-strings
        return f"'{txt}' is not a valid number"

print(string_int('100'))
print(string_int('text'))