lis = [1, 2, 3, 4, 5, 6]
print(lis)
a=lis[0]
for i in range(0, len(lis)-1):
    lis[i]=lis[i+1]
lis[len(lis)-1]=a
print(lis)