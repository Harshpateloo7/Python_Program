#Write correct Python code to complete the following tasks. Do not use any list methods or functions other than len() to accomplish the requested task, use only a loop and indexing (i.e. myList[O]) to solve the requested
#problem.
#Given a list called myList find the sum of all values in the list. Do not worry about the data type, assume that
#"+" will work correctly in the expected way.
myList = [1,2,3,4,5,6,7,8,9,10]

sumOfNumber = 0

for num in myList:
    sumOfNumber = sumOfNumber + num
    
print(sumOfNumber)