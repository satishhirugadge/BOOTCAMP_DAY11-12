# 2. 	Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition 
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average

user=int(input("Choose any number from 1,2,3,4 or 5: "))

if user==1:
    print("Addition")
elif user==2:
    print("Subtraction")
elif user==3:
    print("Division")
elif user==4:
    print("Multiplication")
elif user==5:
    print("Average")

# Ask user to enter the 2 numbers in a variable for first and 
# second for the first 4 options mentioned above.
first=int(input("Enter first number???"))
second=int(input("Enter second number???"))

                  # I am again taking an input fir the operation to be performed.
user1=int(input("Choose any number from 1,2,3,4: "))
if user1==1:
    print(f"Addition: {first+second}")
elif user1==2:
    print(f"Subtraction: {first-second} ")
elif user1==3:
    print(f"Division: {first/second}")
elif user1==4:
    print(f"Multiplication: {first*second}")

# THE BELOW PROGRAM HAS ALL THE TERM ASKED IN TOGETHER.
 # Ask user to enter two more numbers as first1 and 
# second2 for calculating the average as soon as user choose an option 5.

# At the end if the answer of any operation is Negative print a statement saying “zsa”
first1=int(input("Enter first number???"))
second1=int(input("Enter second number???"))

user2=int(input("Choose any number from 1,2,3,4,5: "))
if user2==1:
    add=first1+second1
    print(f"Addition: {add}")
    if add<0:
        print("zsa")
elif user2==2:
    sub=first1-second1
    print(f"Subtraction: {sub} ")
    if sub<0:
        print("zsa")
elif user2==3:
    div=first1/second1
    print(f"Division: {div}")
    if div<0:
        print("zsa")
elif user2==4:
    mul=first1*second1
    print(f"Multiplication: {mul}")
    if mul<0:
        print("zsa")
elif user2==5:
    avg=(first1+second1)/2
    print(f"Average: {avg}")
    if avg<0:
        print("zsa")




