# 7.	Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

num1=[1,3,5,7,9,10]
# print(num1[-1:])  # will give -10 because i havent put the ending tag ...and it is movinng right to left.
# print(num1[-1: :-1]) # if we put the step command also it recognize that it has to be reversed.

#so now lets take only 10 and sdd the othere list to it.
num1[-1:]=[2,4,6,8,"satish","gadge"]   # so I just have selected one element and trying too replace with another list.
 
print(num1)






