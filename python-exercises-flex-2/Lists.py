def numbos():
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
        return enum
print(numbos([2, 3, 4, 5, 6]))
