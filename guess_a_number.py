import random
import sys

def guess(x):
  random_int = random.randint(1, x)
  guess = 0
  
  while random_int != guess:
    guess = int(input(f'Guess a number between 0 and {x}: '))
    if guess < random_int:
      print('Too low. Try Again!')
    elif guess > random_int:
      print('Try Again, Too High')

  print(f'CONGRATS!!! The number was {random_int}')
  sys.exit()


guess(10)