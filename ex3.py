#Write correct Python code to complete the following task. Document all assumptions. Solutions that do not incorporate a loop will receive a grade of O.
#Obtain a positive integer less than 10 from the user and call it d (for divisor). Create a variable called a (for quotient) and give q an initial value of 1000. Divide q by d, saving the result in the variable q. Reduce d by 2.
#Repeat the dividing and reducing steps until either d has become less than or equal to 1, or the variable q is less than 1. Once the loop completes, if q is less than 1 show the message "a small number", otherwise show
#the value of q.
not_less_than_one = True
# Assume users will always input integer number between 0 to 10
d = int(input('Enter your number guess between 0 to 10: '))

q = 1000 #create intial quotient

while not_less_than_one:
    q = q/d
    d= d-2
    if d <=1 or q <1:
        break
        
if q < 1:
    print('a small number')
else:
    print(q)