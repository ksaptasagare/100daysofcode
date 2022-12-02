#number guessing game

#importing the randint method from random module to generate a random integer
from random import randint

#method to run the guessing game, the no of tries are limited to 5
def guess():    
    i = 0
    print(f"You have 5 guesses.\n")
    print("Guess the mystery number(0-100).")
    n = int(input("Number: "))
    rand = randint(1,100)
    while(i<4):
        #giving the user some hints to reduce the attempts
        if(n<rand):
            print("\nYour guess is smaller than the mystery number.")
            n = int(input("Enter again: "))
            i+=1
        elif(n>rand):
            print("\nYour guess is greater than the mystery number.")
            n = int(input("Enter again: "))
            i+=1  
        else:
            print("\nYou guessed the mystery number. It was",rand)
            break
    else:
        print("\nYou have failed to guess the mystery number. It was",rand)
        
#calling the method
guess()
