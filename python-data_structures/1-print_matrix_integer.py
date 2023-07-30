def print_matrix_integer(matrix=[[]]):

    for rows in matrix:
        if not rows:
            print()
            continue

        counting = 0
        
        for items in rows:
            if counting != len(rows) - 1:
                print('{:d} '.format(items), end="")
            
            else:
                print('{:d}'.format(items))
            
            counting = counting + 1

if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])