lis = "mada"
lis = list(lis)
l = len(lis)
for i in range(0,l//2):
    lis[i],lis[l-i-1]=lis[l-i-1],lis[i]
lis = "".join(lis)
print(lis)