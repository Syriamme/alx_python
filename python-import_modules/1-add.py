import sys

if __name__ == "_main_":
    number_args = len(sys.argv) - 1

    arg_list = sys.argv[1:]

    print('Number of argument(s): {}'.format(number_args), end=' ')
    
    if number_args == 1:
        print('argument:', end=' ')

    if number_args == 0:
        print('.')

    else:
        print()

        for i in range(number_args):
            print('{}: {}'.format(i + 1, arg_list[i]))