import random

options = ['rock', 'paper', 'scissors']
Player = input('whats your choice: (rock, paper and scissors): ')
computer = random.choice(options)


def Game():
    # checki the posible outcomes if player chooses rock
    if Player == 'rock':
        if computer == 'paper':
            return 'computer wins'
        elif computer == 'scissors':
            return 'player wins'
        else:
            return 'tie'
    # checki the posible outcomes if player chooses paper
    elif Player == 'paper':
        if computer == 'rock':
            return 'player wins'
        elif computer == 'scissors':
            return 'computer wins'
        else:
            return 'tie'
    # checki the posible outcomes if player chooses scisors
    elif Player == 'scissors':
        if computer == 'rock':
            return 'computer wins'
        elif computer == 'paper':
            return 'player wins'
        else:
            return 'tie'
print('Player choice: ', Player)
print('Computer choice: ', computer)
print(Game())
        