def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # if it's not the last element, print with ' | ' and no newline
            if i != len(row) - 1:
                print('{:d} | '.format(row[i]), end="")
            # if it's the last element, just print the element and newline
            else:
                print('{:d}'.format(row[i]))

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix_integer(matrix)

if __name__ == "__main__":
    main()