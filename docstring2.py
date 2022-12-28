#Complete the examples in the docstring and then write the body of the
#following function:
#def is longer(L1: list, L2: list)-> bool: ""'"Return True if and only if the length of L1 is longer than the length of L2.
#>>> is longer ([1, 2, 31, [4, 5])
#True
#>>> is_ longer((' abcdef'], l'ab', 'cd',"ef'1)
#>>> is longer(l'a',
#'b',
#'c'1, [1, 2, 3]


def is_longer(L1,L2):
    if len(L1) > len(L2):
        return True
    return False

print(is_longer([1,2,3],[4,5]))
print(is_longer(['abcdef'],['ab','cd','ef']))
print(is_longer(['a','b','c'],))