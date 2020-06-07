# 9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

user=int(input("Input a number "))
d = dict()

for x in range(1,user+1):    # (n+1) because range is not taking the last number.  
    d[x]=x*x    # d[x]--key and x*x   is a value

print(d) 
