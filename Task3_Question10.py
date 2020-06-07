# 10. 	Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number. Suppose the following input 
# is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

user=(input("Enter numbers separated by a commas??? : "))

list=user.split(",")
print(list)
print(type(list))  # perfectly!!! list

#now simply convert the list into tuple.
tup=tuple(list)
print(tup)
print(type(tup))


