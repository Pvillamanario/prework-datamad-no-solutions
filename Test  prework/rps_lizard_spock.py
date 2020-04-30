import random


gestures = ('stone', 'paper', 'scissors', 'lizard', 'spock')


max_rounds = int(input('How many rounds do you want to play? Introduce an odd number:'))

while max_rounds%2 == 0:
    max_rounds = int(input('Introduce an odd number: '))
else:
    pass

rounds_to_win = round(int(max_rounds/2),0) + 1


def cpu_toss():

    cpu_gesture = random.choice(gestures)
    return cpu_gesture


def player_toss():

    player_gesture = input('Make your move!! stone, paper, scissors, lizard or spock?: ')
 
    while player_gesture.lower() not in gestures:
        
        player_gesture = input("I didn't get it... Try again, please... stone, paper, scissors, lizard or spock?: ")
    
    else:
        
        return player_gesture



def combat():
    
    all_toss = {('stone', 'stone'): 0, ('stone', 'lizard'): 1, ('stone', 'spock'): 2, ('stone', 'scissors'): 1, ('stone', 'paper'): 2,
            ('lizard', 'stone'): 2, ('lizard', 'lizard'): 0, ('lizard', 'spock'): 1, ('lizard', 'scissors'): 2, ('lizard', 'paper'): 1,
            ('spock', 'stone'): 1, ('spock', 'lizard'): 2, ('spock', 'spock'): 0, ('spock', 'scissors'): 1, ('spock', 'paper'): 2,
            ('scissors', 'stone'): 2, ('scissors', 'lizard'): 1, ('scissors', 'spock'): 2, ('scissors', 'scissors'): 0, ('scissors', 'paper'): 1,
            ('paper', 'stone'): 1, ('paper', 'lizard'): 2, ('paper', 'spock'): 1, ('paper', 'scissors'): 2, ('paper', 'paper'): 0,
            }

    toss = (cpu_toss(), player_toss()) 

    print('CPU: {} \nPlayer: {}'.format(toss[0], toss[1]))

    global result
    result = all_toss[toss]
    return result


def status():
    
    if result == 0:
        print('Tie!')
    elif result == 1:
        print('CPU wins!')
    elif result == 2:
        print('Player wins!')
    else:
        print('Ooooops!')



def game():

    cpu_score= 0
    player_score = 0
    rounds = 0

    while rounds < max_rounds:

        if (cpu_score == rounds_to_win or player_score == rounds_to_win): 
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
        print('Players wins the game!!!')
    
    else:
        print('There has been a tie!!')



game()