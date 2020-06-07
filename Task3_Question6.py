# 6.	Create a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30 (both included).

list=[1,2,3,4,5,6,7,8,9,10]
#print(list[:5])
#print(list[-5:])

list1=[*range(1,31)]
print(list1)

lis=[]

for i in list1:
    lis.append(i*i)

x=lis[:5]
y=lis[-5:]
z=x+y
print(z)

