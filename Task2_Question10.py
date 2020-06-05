# 10. Write a program that asks five times to guess the lucky number.
#  Use a while loop and a counter, such as
#            		counter=1
# 		While counter <= 5:
# 			print(“Type in the”, counter, “number”
# 			counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not).
#  If the correct number is guessed, the program outputs “Good guess!”, otherwise it 
#  outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.


#let set the winning value.
winning_value=14 # as 14 is my lucky number.
game_over=False # as intially the game is not over so we have to set it as false.
counter=0
#take the input value from the user  which I am taking from 1 tp 20
user_num=int(input("Guess your lucky number between 1 to 20??? :"))

while not game_over:
    if user_num==winning_value:
        print("Good Guess!!!") 
        break
     
       
    elif user_num!=winning_value:
        user_num=int(input("Guess your lucky number between 1 to 20??? :"))
        counter=counter+1
        if counter==4:  
            print("Five wrong Guess!!! You ar out")
            break
        

              

            

  








