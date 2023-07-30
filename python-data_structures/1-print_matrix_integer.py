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
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(print_matrix_integer(matrix))