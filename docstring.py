#Complete the examples in the docstring and then write the body of the
#following function:
#def same first last L: list)
#""'"''Precondition: Len L) >= 2-> bool:
#Return True if and only if first item of the list is the same as the last.
#>>> same_first_ last([3, 4, 2, 8, 31)
#True
#>>> same_first_last(l'apple'
#banana
#>>> same first_last ((4.0, 4.5])'pear'])
def same_first_last(L):
    if len(L) >= 2:
        if L[0] == L[-1]:
            return True
    return False

print(same_first_last([3,4,2,8,3]))
print(same_first_last([4.0,4.5]))