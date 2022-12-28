#Write correct Python code to complete the following tasks. Do not use any list methods or functions other
#than len( to accomplish the requested task, use only a loop, if needed, and slicing (i.e. myList[0:1]) to solve the
#requested problem.
#Given a list called myList and a value called findme, remove the first copy of findme from myList, if it is in the
#list. Do not worry about the data type, assume that "=="will work in the expected way.
myList = [1,2,3,4,5,6,7,8,9,10,6]
findMe = 6

for i in myList:
    if i == findMe:
        new_list = myList[0:myList.index(i)]
    
    continue_list = myList[myList.index(i)+1:]
    break
    
final_list= new_list + continue_list
print(continue_list)