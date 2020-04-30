# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

import random

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.

gestures = ('stone', 'paper', 'scissors')

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...

max_rounds = 5

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

rounds_to_win= 3

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.

def cpu_toss():

    cpu_gesture = random.choice(gestures)
    return cpu_gesture

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.

def player_toss():

    player_gesture = input('Make your move!! stone, paper or scissors?: ')
 
    while player_gesture.lower() not in gestures:
        
        player_gesture = input("I didn't get it... Try again, please... stone, paper or scissors?: ")
    
    else:
        
        return player_gesture
    
# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
 
def combat():
    
    all_toss = {('stone', 'stone'): 0, ('stone', 'paper'): 2, ('stone', 'scissors'): 1,
            ('paper', 'stone'): 1, ('paper', 'paper'): 0, ('paper', 'scissors'): 2,
            ('scissors', 'stone'): 2, ('scissors', 'paper'): 1, ('scissors', 'scissors'): 0
            }

    toss = (cpu_toss(), player_toss()) 

    print('CPU: {} \nPlayer: {}\n'.format(toss[0], toss[1]))

    global result
    result = all_toss[toss]
    return result

# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated

def status():
    
    if result == 0:
        print('Tie!\n\n')
    elif result == 1:
        print('CPU wins!\n\n')
    elif result == 2:
        print('Player wins!\n\n')
    else:
        print('Ooooops!')
        
# Create two variables that accumulate the wins of each participant
# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.
# Print by console the winner of the game based on who has more accumulated wins

def game():

    cpu_score= 0
    player_score = 0
    rounds = 0

    while rounds < max_rounds:

        if (cpu_score == 3 or player_score == 3): 
            break
                
        else:

            rounds += 1
            combat()
            status()

            if result == 1:
                cpu_score +=1

            elif result == 2:
                player_score +=1
            
            else:
                pass

    
    if cpu_score > player_score:
        print('CPU wins the game!!!')
    
    elif cpu_score < player_score:
        print('Player wins the game!!!')
    
    else:
        print('There has been a tie!!')
        
        
game()