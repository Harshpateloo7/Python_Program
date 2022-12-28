correct_input = True
lst = []
while correct_input:
    user_input = input('Enter your input: ')
    if user_input.lower() == 'I am done'.lower():
        break
    elif user_input.isspace():
        user_input = input('Try Again: ')
    lst.append(user_input) 

print(sorted(lst, reverse=True))