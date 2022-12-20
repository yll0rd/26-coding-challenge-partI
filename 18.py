def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
   
print("The first 100 prime numbers are:\n")
count=0
i=0
while count<100:
    if isprime(i) == True:
        print(i, end=" ")
        count+=1
    i+=1
    
#print(f"\n{count}")
    
    
    
    