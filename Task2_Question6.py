# 6. What is the output of the following code examples?

# x=123 
#   for i in x:
#     print(i)

# So logically the answer will be unecpected intend but if we settle up the indendation it will 
# give the error as the type error and to settle the we need to do the following way.
x="123"
for i in x:
    print(i)



i = 0   #i starts from 0
while i < 5:  # and ends at 5
    print(i)     #it prints the i
    i += 1        #increament after the print
    if i == 3:     # condition that if i==3 then it breaks 
        break
else:
    print("error")     # as we have alreday define i as 0 there is no use of this statment but if 
                        #we change the i value and make it above 5 then this statment will run.

# out put: 0 1 2



# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break             here the break spelling itself is wrong so shows an error
                         # but ie we clear the spellinf the output will be

                         #output: 0 1 2 3 4 (as it start from 1 make an increament of 1 and break at >=5)
