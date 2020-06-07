# 5. 	Create a new list which contains the specified numbers after removing 
# the even numbers from a predefined list. 

# in short we have to remove all the odd numbers.

list=[1,2,3,4,5,6,7,8,9,10]
lis2=[]
for i in list:
    if i%2!=0:
        lis2.append(i)

print(lis2)








