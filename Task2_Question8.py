# 8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

user=input("Enter the string mixed with the numbers???")

digit=0
letter=0
for character in user:
    if character.isdigit():
        digit=digit+1
    elif character.isalpha():
        letter=letter+1
   
print(user)    
print("Letters ", letter)
print("Digits ", digit)






