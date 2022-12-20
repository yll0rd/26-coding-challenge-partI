def extend_3(a,b):
    c=[]
    print(a)
    print(b)
    for i in a:
       if i not in b:
           c.append(i)
    return c
    
print(extend_3([1,2 ,5],[5,4]))