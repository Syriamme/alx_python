def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Inputs should be integers.")
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("No result due to error.")
    return result
