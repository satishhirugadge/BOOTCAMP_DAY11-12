# 9. Read the two parts of the question below: 
#  Write a program such that it asks users to “guess the lucky number”.
#   If the correct number is guessed the program stops, otherwise it continues forever. 

# Modify the program so that it asks users whether they want to guess again each time. 
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question
#  whether they want to continue guessing. The program stops if the user guesses the 
#  correct number or answers “no”. ( The program continues as long as a user has not
#   answered “no” and has not guessed the correct number)

#let set the winning value.
winning_value=14 # as 14 is my lucky number.
game_over=False # as intially the game is not over so we have to set it as false.

#take the input value from the user  which I am taking from 1 tp 20
user_num=int(input("Guess your lucky number between 1 to 20??? :"))

while not game_over:
    if user_num==winning_value:
        print("Congratulations,You won the game!!!")
        game_over=True      # this helps to come out if the game is over or else it will keep on running.

    else:
        print("You Lost the game !!!")
  
        user=input("Guess again??? answer in 'yes' or 'no' :")
        if user=="yes":
            user_num=int(input("Guess your lucky number between 1 to 20??? :"))
        elif user=="no":
            print("You Lost the game!!!")
            game_over=True    # this helps to come out if the game is over or else it will keep on running.

