from math import sqrt

print("The first 10 fibonacci numbers are:")
for i in range(11):
    a= (1+sqrt(5))**i - (1-sqrt(5))**i
    b= sqrt(5)*2**i
    print(f"{round(a/b)}", end=" ")