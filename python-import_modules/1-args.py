import sys

def print_args_info():
    argv = sys.argv
    num_args = len(argv) - 1

    if num_args > 0:
        print(f"Number of arguments: {num_args}:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
    else:
        print("Number of arguments: 0.")

if __name__ == "__main__":
    print_args_info()