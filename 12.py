def convertpos(n):
    j=0
    for i in n:
        if i < 0:
            n[j]=n[j]*-1
        j+=1
    return n
    
    
print(convertpos([1, 2, 3, -5]))