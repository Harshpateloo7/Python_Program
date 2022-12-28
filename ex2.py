#Write correct Python code to complete the following task. Document all assumptions. Solutions that do not incorporate a loop will receive a grade of O.
#Create a loop that will build a string with all of the even numbers between 3 and 10001 inclusive from
#greatest to least. Print the string after the loop has ended.
# range function return value until 'last number-1'. Hence add +1 to make 10001 inclusive.
# map function can help convert all list integers into strings and return iterator
#using join function, we can concat all list items into string.
# Use of reversed function will return reverse iterator object
lst = []
for num in range(3, 10001+1):
      
    if num % 2 == 0:
        lst.append(str(num))

revesed_lst = list(reversed(lst))
str1 = ''.join(map(str, revesed_lst))
print(str1)