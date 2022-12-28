#define a funcation that has one parameter, a number, and returns the number tripled.

def tripled(x):
    return x *3

#Define a function that has four parameters, all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades.

def av_g(g1,g2,g3):

    sum=g1+g2+g3

    return sum/3
print (sum)

def average3HighestGrades(a,b,c,d):

    minGrade =min(a,b,c,d)
    sumGrade = a+b+c+d -minGrade
    average = sumGrade/3
    return average

num =average3HighestGrades(55,60,65,45)

print (num)
    
