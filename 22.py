lis = [1,2,3,4,5,6]
l = len(lis)
for i in range(0,l//2):
    lis[i],lis[l-i-1]=lis[l-i-1],lis[i]
    
print(lis)