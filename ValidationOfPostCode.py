def validatePostalCode(code):
    if len(code) > 7:
        return False
    if not (code [0].isalpha() and code[1].isdecimal() and code[2].isalpha()):
        return False
    if (code[3].isspace()):
        if not(code[4].isdecimal() and code[5].isalpha() and code[6].isdecimal()):
            return False
    elif len(code) > 6:
        return False
    else:
        if not (code[3].isdecimal() and code[4].isalpha() and code[5].isdecimal()):
         return False
    return True    

postalCode = input("Enter a postal code:")
postalCodeValid = validatePostalCode(postalCode)

while not postalCodeValid:
    postalCode = input("Invalid code!! Try again:")
    postalCodeValid = validatePostalCode(postalCode)
print("Congrats!!")

#A1B2C3 should be valid
#A1B 2C3 is also valid