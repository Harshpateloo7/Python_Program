size=7

for r in range(1, size+1,1):
    row=''
    for c in range(1, size-r+1,1):
        row+=''
        for c in range(size-r, size,1):
            row+='T'
            print(row)
        
