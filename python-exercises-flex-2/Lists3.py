def poop(p, o):
    el = []
    for i in range(len(p)):
        MyList = p[i] * o[i]
        el.append(MyList)
    return el
    
    
name1 = [2, 3, 4]
name2 = [4, 5, 6]
print(poop(name1, name2))