def isUppercase(x):
    ''' Checks if any of the characters is uppercase (1 argument necessary) '''
    if any(a.isupper() for a in x):
        return True
    else:
        return False

def isLowercase(x):
    ''' Checks if any of the characters is lowercase (1 argument necessary) '''
    if any(a.islower() for a in x):
        return True
    else:
        return False

def isSpace(x):
    ''' Checks if any of the characters is a whitespace (1 argument necessary) '''
    if any(a.isspace() for a in x):
        return True
    else:
        return False

def isSymbol(x):
    ''' Checks if any of the characters is a symbol (1 argument necessary) '''
    if any(not a.isalnum() for a in x):
        return True
    else:
        return False

def isspace_and_alpha(x):
    ''' Checks if any of the characters is a letter or a space (1 argument necessary) '''
    if any(a.isspace() for a in x) or any(a.isalpha() for a in x):
        return True
    else:
        return False

def isNumeric(x):
    ''' Checks if any of the characters is a number (1 argument necessary) '''
    if any(a.isdigit() for a in x):
        return True
    else:
        return False

def isUCAS_codes_approved(x):
    ''' Checks if the string is conform to UCAS codes
    which consist of 1 letter
    and ends with 3 numbers (1 argument necessary) '''
    custom_tuple = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    if any(a.endswith(custom_tuple, 0, 5) for a in x):
        return True
    else:
        return False
