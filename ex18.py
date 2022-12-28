numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['(', ')', '-']

def numberChecker(number_string):
    
    if (len(number_string) == 10) and (number_string.isnumeric()):
        return True
        
    elif number_string[3] in special_characters:
        for index, number in enumerate(number_string):
            if index in [3,7]:
                if number not in special_characters:
                    return False
            else:
                return True
    else:
        return False
print(numberChecker("123-456-7890"))