def gpa_calculator(a,b,c,d):
    avg = (a+b+c+d)/4
    avg =100* avg/50

    if avg>=85:
        return'A'
    elif avg>=75:
        return'B'
    elif avg>=65:
        return'c'
    elif avg>=50:
        return'D'
    else:
        return'F'
