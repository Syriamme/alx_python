import sys

def main():
    arguments = len(sys.argv) - 1
    list = sys.argv[1:]

    print("Number of arguments: {}".format(arguments), end=" ")
    if arguments == 1:
        print("argument:", end=" ")
    else:
        print("arguments: ", end=" ")

    if arguments == 0:
        print(".")

    else:
        print()
        
    for i in range(num_arguments):
        print(f'{i + 1}: {arguments_list[i]}')

if __name__ == "__main__":
    main()