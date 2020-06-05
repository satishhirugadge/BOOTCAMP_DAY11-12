# 4. 	Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”



var =int(input("Enter a number from 5 to -5 :"))                  
while var > 0:              
   print ("Current variable value : ", var)
   var = var -1
   if var == 0:
      break

print("Its over!") 


var1 =int(input("Enter a number from 5 to -5 :"))                  
while var1<=10 :              
   print ("Current variable value : ", var1)
   var1 = var1 +1
   if var1 == 5:
      continue

print("Its over!") 



   
   
    

