# ASSUME user enters a positive number with at most 2 decimal places
# READ a number from the user AS income
income = input( "How much is the income? " )
income = float( income )
# ASSUME user enters a positive number with at most 2 decimal places
# READ a number from the user AS savings
savings = float( input( "How much is the savings? " ) )
# ASSUME user enters a positive number with at most 2 decimal places
# READ a number from the user AS rent
rent = input( "How much is the rent? " )
rent = float( rent )
# ASSUME user enters a number with at most 2 decimal places
# READ a number from the user AS bills
bills = input( "How much are the bills? " )
bills = float( bills )
# CALCULATE income + savings AS assets
assets = income + savings
# CALCULATE rent + bills AS expenses
expenses = rent + bills
# CALCULATE assets - expenses AS money left over
money_left_over = assets - expenses
# CALCULATE money left over > 0 AS decision
decision = money_left_over > 0
# SHOW "It is", decision, "that Bobbie has enough money left over to go out."
print( "It is", decision, "that Bobbie has enough money left over to go out." )
