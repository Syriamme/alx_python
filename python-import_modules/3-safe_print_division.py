def safe_print_division(a, b):
    
    try:
        division_result = a / b

    except ZeroDivisionError:
        return None
    
    finally:
        print("Inside result:: {}".format(division_result))

    return division_result