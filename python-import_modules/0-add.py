def add(a, b):
    return (a + b)

a = 1
b = 2
from add_0 import add

adding = add(a, b)

if __name__ == "_main_":
    print("{} + {} = {}".format(a, b, adding))