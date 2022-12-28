def triangle(lines):
    
    for row in range(0, lines):
        line = ''
        for column in range(0, row+1):
            line +='*'
        print(line)

lines = 6
triangle(lines)