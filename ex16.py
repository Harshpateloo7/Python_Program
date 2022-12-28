binaryString = input('Enter Binary String: ')
n = len(binaryString)- 1
print(n)

exp = 0
value = 0

if n <0:
    print(value)
else:
    digit = binaryString[n]
    
    if digit == 1:
        value = (value + 2)**exp
        exp = exp + 1
        n = n-1
        print(value)
    else:
        exp = exp + 1
        n = n-1
        print(value)