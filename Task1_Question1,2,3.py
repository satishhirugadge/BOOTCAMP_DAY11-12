# 1.	Create three variables in a single a line and assign different 
# values to them and make sure their data types are different. Like one is 
# int, another one is float and the last one is a string.

a=10
b=10.14
c="Satish"

print(type(a))
print(type(b))
print(type(c))

# 2. 	Create a variable of value type complex and swap it with 
# another variable whose value is an integer.

d= 50 + 3j  
print(type(d))  #complex

b=d   #here I swap the value of d with the b and then printed
print(b)

# 3 Swap two numbers using the third variable as the result name
#  and do the same task without using any third variable.
a1=10
b1=5
result=a1
a1=b1
b1=result
print(a1)   #5
print(b1)   #10









