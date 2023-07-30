def no_c(my_string):
    
    removed = []
    
    for char in my_string:
        if char not in ('c', 'C'):
            removed.append(char)
    return ''.join(removed)

if __name__ == "__main__":
    print(no_c("My Computer is cooling down"))