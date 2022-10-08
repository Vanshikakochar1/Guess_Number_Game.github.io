
'''
Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.

Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue,
and his score gets reduced. 

The clue can be multiples, divisible, greater or smaller, or a combination of all.

'''
import random
import math

print("Hello! What's your name?")

my_name = input()

# User takes inputs
lower_bound = int(input("Enter lower bound:")) # User enters the starting value

upper_bound = int(input("Enter upper bound:")) # User enters the last value of the range
# This is used to genrate a random number between the lower and upper limits
random_generator = random.randint(lower_bound, upper_bound)
print('Well, ' + my_name + ', I am thinking of a number between' + "" +str(lower_bound) + "" +'and' + "" + str (upper_bound ))

# Initializing the number of guesses
guess_taken = 0
'''
module “math” which allows us to compute logs using a single line.
'''
while guess_taken < math.log(upper_bound - lower_bound + 1, 2):
    guess_taken += 1
    # Input values in guess variable
    guess = int(input("Take a guess :"))
    guess_taken = guess_taken+1

    # Applying the condition
    if random_generator == guess:
        print("Well done," +my_name + "! You guessed the number in " + guess_taken + "Guesses!")
        # If it is guessed in 1 try then the loop will break
        break
    elif random_generator > guess:
        print("Your guess is too small!")
    elif random_generator < guess:
        print("Your guess is too high!")

'''
If the guessing limit is exceeded by the required guesses,
then show this output
'''       

if guess_taken >= math.log(upper_bound - lower_bound +1 , 2):
    print("\n The number I was thinking was %d " %random_generator )
    print(" \n \t Better luck next time!")
