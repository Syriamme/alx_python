import sys

def print_args_info():
    argv = sys.argv
    num_args = len(argv) - 1  # Subtract 1 because argv[0] is the script name itself

    if num_args > 0:
        arg_suffix = "argument:" if num_args == 1 else "arguments:"
        print(f"{num_args} {arg_suffix}")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
    else:
        print("0 arguments.")

if __name__ == "__main__":
    print_args_info()
