# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to 
# guess which item in the list was selected. Use random.choice() to 
# select the item and take the user's guess via input. Provide feedback
# on whether they guessed correctly or not.

import random

genre = ['shooter', 'horror', 'puzzle', 'adventure', 'arcade']

answer = random.choice(genre)

while True:
      pick = input('Guess the Genre of the video game!')
      if pick == answer:
            print('You guessed correctly! the Genre was: ' + answer)
            break
      else:
            print('Good guess but the correct answer was: ' + answer)
      