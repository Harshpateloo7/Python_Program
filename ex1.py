#Write correct Python code to complete the following task. Document all assumptions. Solutions that do not
#incorporate a loop will receive a grade of ..A
#Create a loop that will build a string with all of the odd numbers between 3 and 10001 inclusive. Print the string after the loop has ended.
lst = []
for num in range(3, 10001+1):
      
    if num % 2 != 0:
        lst.append(str(num))
        
str1 = ''.join(map(str, lst))
print(str1)