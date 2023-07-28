import sys

def main():

    argument = sys.argv

    arg_list = len(argument) - 1

    if arg_list > 0:

        names = "argument:" if arg_list == 1 else "arguments:"

        print(f"{arg_list} {names}")

        for i in range(1, len(argument)):

            print(f"{i}: {argument[i]}")
    else:
        print(".")

if __name__ == "__main__":
    main()