gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

gandalf_wins = 0
saruman_wins = 0
spells = 0

clash = tuple(zip(gandalf, saruman))

print(clash)

for i in clash:

    if i[0]>i[1]:
        gandalf_wins +=1
    else:
        saruman_wins +=1

print(gandalf_wins,'-', saruman_wins)

if gandalf_wins > saruman_wins:
    print('Gandalf wins') 

elif gandalf_wins < saruman_wins:
    print('Saruman wins') 

else:
    print('Tie')

######################################

POWER = {'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

gandalf_power = []
saruman_power = []

for i in gandalf:
    gandalf_power.append(POWER[i])

for i in saruman:
    saruman_power.append(POWER[i])

print(gandalf_power)
print(saruman_power)


gandalf_wins = 0
saruman_wins = 0
rounds = 0

clash = tuple(zip(gandalf_power, saruman_power))

for i in clash:
    if i[0] > i[1]:
        gandalf_wins += 1
        saruman_wins = 0
        rounds += 1
    
    elif i[0] < i[1]:
        gandalf_wins = 0
        saruman_wins += 1
        rounds += 1

    else: 
        pass

if gandalf_wins > saruman_wins:
    print('Gandalf wins in {} rounds.'.format(rounds))

else:
    print('Saruman wins in {}'.format(rounds))


gandalf_avg_power = sum(gandalf_power)/len(gandalf_power)
saruman_avg_power = sum(saruman_power)/len(saruman_power)

print("Gandalf's average magical power is {}".format(gandalf_avg_power))
print("Saruman's average magical power is {}".format(saruman_avg_power))


s = 0 
for i in gandalf_power:
    s += (i-gandalf_avg_power)**2
gandalf_std_dev = (s/len(gandalf_power))**0.5 

s = 0 
for i in saruman_power:
    s += (i-saruman_avg_power)**2
saruman_std_dev = (s/len(saruman_power))**0.5 

print(gandalf_std_dev)
print(saruman_std_dev)