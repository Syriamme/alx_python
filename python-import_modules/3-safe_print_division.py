def safe_print_division(a, b):
    result = None

    try:
        result = a / b
        
    except Exception as n:
        pass
    
    finally:
        print("Inside result: {}".format(result))

    return result