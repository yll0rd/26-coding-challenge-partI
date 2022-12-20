fact10=1
list = range(11)
list = list[11:0:-1]
for i in list:
   fact10*=i
    
print(f"10! = {fact10}")