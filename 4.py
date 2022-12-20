last = int(input("Enter the last number of multiplication number: "))
for i in range(11):
    for j in range(last+1):
        print(f"{i} * {j}  = {i*j}")
    print('')