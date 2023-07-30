def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        counter = 0
        for item in row:
            if counter != len(row) - 1:
                print('{:d} '.format(item), end="")
            else:
                print('{:d}'.format(item))
            counter += 1

if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])