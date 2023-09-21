import random
import time
print('''[ 0 ] ROCK
[ 1 ] PAPER 
[ 2 ] SCISSOR ''')
option = int(input('Your choice: '))
machine = ('Rock', 'Paper', 'Scissors')
rand = random.choice(machine)
game = ''
if option == 0:
    option = 'Rock'
elif option == 1:
    option = 'Paper'
elif option == 2:
    option = 'Scissors'
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
if machine == 'Rock' and option == 'Rock' or machine == 'Paper' and option == 'Paper' or machine == 'Scissors' and option == 'Scissors':
    game = 'Draw!'
elif machine == 'Rock' and option == 'Scissors' or machine == 'Paper' and option == 'Rock' or machine == 'Scissors' and option == 'Paper':
    game = 'Machine Wins!'
elif option == 'Rock' and machine == 'Scissors' or option == 'Paper' and machine == 'Rock' or option == 'Scissors' and machine == 'Paper':
    game = 'Player Wins!'
print('-='*15)
print(f'Computer choice: {rand}')
print(f'Player choice: {option}')
print('-='*15)
print(game)
