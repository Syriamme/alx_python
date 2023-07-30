def no_c(my_string):
    
    new_strng = []
    
    for char in my_string:
        if char not in 'cC':
            new_strng.append(char)
            
        return ''.join(new_strng)