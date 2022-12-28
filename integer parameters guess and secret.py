import random

Secret_Guess = int(random.randint(97,122))
print('Secret Guess:',Secret_Guess)
User_Guess = int(input("Enter User guess:"))

def clean_userinput(User_Guess):
    is_wrong_input = True
    
    while is_wrong_input:
        User_Guess = User_Guess.lower()
    
        if len(User_Guess) > 1:
            User_Guess = input('You have entered more than one letter. Try again: ')
        
        elif not User_Guess.isalpha():
            User_Guess = input('You can only enter single letters. Try again: ')
            
        else:
            break
    
    return User_Guess




def checkGuess(User_Guess, Secret_Guess):
    
    if (User_Guess) > (Secret_Guess):
        return '1.'

    elif (User_Guess) <(Secret_Guess):
        return '-1'

    else:
        return '0'

