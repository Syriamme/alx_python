def validate_password(password):

    if len(password) < 8:
        return False
    
    _uppercase = any(char.isupper() for char in password)
    
    _digit = any(char.isdigit() for char in password)
    
    _lowercase = any(char.islower() for char in password)
    
    if not (_uppercase and _lowercase and _digit):
        return False
    
    if ' ' in password:
        return False

# if everything is okay return true
    return True