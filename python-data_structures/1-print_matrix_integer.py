def print_matrix_integer(matrix=[[]]):
    
    for rows in matrix:
        
        for columns in rows:
            
            print("{:d}".format(columns), end=" ")
        
        print()
        
if __name__ == "__main__":
    testing_matrix = [
        [1, 9, 10, 14],
        [3, 9, 16, 22],
        [60, 27, 59, 88]
    ]

print_matrix_integer(testing_matrix)