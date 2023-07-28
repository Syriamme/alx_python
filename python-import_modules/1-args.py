import sys

if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    list = sys.argv[1:]

    print('Number of arguments: {}'.format(arguments), end='')
    if arguments == 1:
        print('argument:', end=' ')
    else:
        print('arguments:', end=' ')

    if arguments == 0:
        print(".")

    else:
        print()

        for i in range(arguments):
            print("{}: {}".format(i + 1, list[i]))