# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#        Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

counter=0
while counter<=6:
    
    if counter==3:
        counter=counter+1  # this is the must statment or else it wont work
        continue
    if counter==6:
        break
    print(counter)
    counter+=1
    
    
    
    
    





