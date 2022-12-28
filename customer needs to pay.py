#I Harshadkumar Patel, 000852665, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

import random

# set base amount for coins
quaters = .25
dimes = 0.10
nickels = 0.05
 
# set a random amount
amount = round(random.randint(0,20) + round( random.randint(0,100)/100, 2 ),2)
print('Amount you owe: ', amount)   

# accept only number as a amount of payment
def check_amount_of_payment(inpt):
    is_wrong_input = True
    while is_wrong_input:
        try:
            inpt = int(inpt)
            break
        except:
            try:
                inpt = float(inpt)
                break
            except:
                inpt = input("That's not correct amount-enter again: ")
                
    return inpt

# calculate each coin type to return
def calculate_change(coins, coin_name):
    
    if coins/coin_name >= 1:
        actual_coins = coins//coin_name
        remainder = coins - (actual_coins * coin_name)
        return (actual_coins, round(remainder,2))
    else:
        return (0, coins)


# ask to enter amounts for payment
amount_of_payment = check_amount_of_payment(input('Enter your amount: '))

# if amount is greater then payment - no change is required
if amount > amount_of_payment:
    print('No change owed')

# calculate change if payment is greater than amount
else:
    d,q,i,n = 0,0,0,0
    amount_back = amount_of_payment - amount
    d, change = divmod(amount_back,1)

    if change > 0:
        q, remainder = calculate_change(change, quaters)
        i, remainder = calculate_change(remainder, dimes)
        n, remainder = calculate_change(remainder, nickels)
        round_penny_to_nickels = (round(remainder*2,1)* 10)
        n += round_penny_to_nickels
    
    #print final change
    print(f'You got {d} dollars, {q} quaters, {i} dimes, {n} nickels back in change.')
