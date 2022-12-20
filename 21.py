lis = [1, 2, 3, 4, 5, 6]
print(lis)
a=lis[len(lis)-1]
l=range(len(lis)-1)
for i in l[len(lis)-1::-1]:
    lis[i+1]=lis[i]
    print(lis)
lis[0]=a
print(lis)