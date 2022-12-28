#Test Average and Grade

#Enter 5 test scores
a = int(input('Enter score a: '))
b = int(input('Enter score b: '))
c = int(input('Enter score c: '))
d = int(input('Enter score d: '))


total =(a + b + c + d )

#Calculate average
def calc_average(total):
    return total / 4

#Grading scale
def determine_score(grade):
    if 85>= grade:
        return 'A'
    elif 75>= grade <85:
        return 'B'
    elif 65>= grade <75:
        return 'C'
    elif 50>= grade <65:
        return 'D'
    else:
        return 'F'


grade = total
avg = calc_average(total)
abc_grade = determine_score(grade)

print("That's a(n): " + str(abc_grade))
print('Average grade is: ' + str(avg))
