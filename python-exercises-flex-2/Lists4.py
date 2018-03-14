Dlist1 = [[1, 3, 5],
         [4, 5, 6]]
Dlist = [[2, -2, 7],
         [5, 3, 7]]
def poop(p, o):
    el = []
    el2 = []
    
    for i in range(len(p)):
        for j in range(len(p[0])):
            MyList = Dlist1[i][j] + Dlist[i][j]
            el.append(MyList)
        el2.append(el)
    return el
  
         
print(poop(Dlist1, Dlist))
   