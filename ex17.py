dct = {'a': 0, 'e': 0, 'i': 0, 'o':0, 'u':0}
lst = ['aeiuo',  'that', 'aaaaa' ,'uuuu']

for words in lst:
    for word in words:
        word = word.lower()
        if word in dct:
            dct[word] +=1
        
print(f"{dct['a']} a's, {dct['e']} e's, {dct['i']} i's, {dct['o']} o's, {dct['u']} u's")