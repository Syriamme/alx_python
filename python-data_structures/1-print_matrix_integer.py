def print_matrix_integer(matrix=[[]]):
    
    for rows in matrix:
        
        for columns in rows:
            
            print("{:d} ".format(columns))
        
        print()