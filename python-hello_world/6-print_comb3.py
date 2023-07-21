for num1 in range (10):
    for num2 in range (num1 + 1, 10):
        if num1 != 9 or num2 != 10:
            print ("{:}".format(num1), "{:}".format(num2), end=", ")