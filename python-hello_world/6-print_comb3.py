for num1 in range (10):
    for num2 in range (num1 + 1, 10):
        print("{}{}".format(num1, num2), end=", "if num1 != 8 or num2 != 9 else "\n")