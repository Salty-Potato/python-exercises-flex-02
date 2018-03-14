words = 'hello world'
for leet in words:
    if leet == 'h':
        print(2)
    elif leet == 'e':
        print(3)
    elif leet == 'l':
        print(4)
    elif leet == 'o':
        print(5)
    elif leet == 'w':
        print(7)
    elif leet == 'r':
        print(8)
    else:
        
        print(leet)

s = "A string"


# leet = {'a': '4', 's': '3', 'i': '1', 't': '0', 'r': '4', 'n': '3', 'g': '1', 'A': '0'}
for k, v in leet.items():
    s = s.replace(k, v)

print(s)