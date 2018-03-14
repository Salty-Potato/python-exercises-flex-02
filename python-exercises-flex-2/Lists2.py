def numbos(l):
    enum = []
    for n in l:
        if n > 0:
            print(n)
            enum.append(n)
    return enum

numbo = [-2, -3, -4, 1, 3]
print(numbos(numbo))