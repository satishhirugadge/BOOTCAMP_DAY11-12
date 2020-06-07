# 3.  Write a program to get the sum and multiply of all the items in a given list.

list=[1,2,3,4,5]
# we have to perform the sum and multiple of this all number.
def sum():
    result=0     # here we stareted with 0 be cause e want to add it
    for i in list:
        result+=i
    print(result)
sum()

#Multiplication.
list1=[1,2,3,4,5]
def mul():
    result=1   # if we put 0 then anything multiply by 0 will give 0
    for j in list1:
        result*=j
    print(result)
mul()










