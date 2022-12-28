def countExamWordOccurrences(sentence):
    len = 0
    for char in sentence:
	    len = len + 1     

    counter = 0
    
    for i in range(0, len - 3):
       str = sentence[i] + sentence[i+1] + sentence[i+2] + sentence[i+3]
       if str.lower() == "exam" :
           counter = counter + 1
       
    return counter 
    

val = countExamWordOccurrences("eexamwEbamaienqe.am")
print(val)