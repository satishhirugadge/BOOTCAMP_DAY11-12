# 6. 	Write a program to check the data type of the entered values. 
# HINT: Printed output should say -  The input value data type is: int/float/string/etc

a=10
b=10.14
c="Satish"
d=True

print(f"The input value data type is: {type(a)}")
print(f"The input value data type is: {type(b)}")
print(f"The input value data type is: {type(c)}")
print(f"The input value data type is: {type(d)}")

# 7. 	If one data type value is assigned to ‘a’ variable and then a different data 
# type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?

a=5
a=6
print(a) # this term is called as the type mutation. where we can change the value, and it picks
#the last value.
