# This is my first game to guess the correct number - It's random guess and no maths behind
import random
import math

guess = random.randint(1, 100)
# print(guess)
# take input from user
# user_input =[0]
user_input = int(input('Welcome to Guess Number & Win a lucky Price Game ! \nGuess your number , lets see ! '))
print(user_input)


def myFunc(user_input):
    retry_count = 0
    while user_input < 0 or user_input > 100:
        print('Select numbers in the range of 1 & 100 ')
        user_input = int(input('Guess your number , lets see ! '))
        retry_count += 1
        if retry_count >= 2:
            print('Reached maximum attempts')
            break


myFunc(user_input)

if user_input == guess:
    print('You Nailed it...!')
else:
    print('Better luck next time ')
