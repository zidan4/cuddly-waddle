import random
import sys

player = input("Enter your choice: \n 1 for rock\n 2 for paper or \n 3 for scissors): \n")
player = int(player.lower())
#print(player)

if player < 1 or player > 3:
  print('You did not pick rock/paper/scissors')
  sys.exit()

computer = int(random.choice('123'))
print(f'Computer chose {computer}')
print(f'You chose {player}')

if player == 1 and computer == 3:
  print('You Win!')
elif player == 2 and computer == 1:
  print('You Win')
elif player == 3 and computer == 2:
  print('You Won')
elif player == computer:
  print('Tie Game!')
else:
  print('Conputer Wins')