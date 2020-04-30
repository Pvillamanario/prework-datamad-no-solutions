bus_stop = (0, 0)
n_personas = []
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
total = 0
n_stops=len(stops)

for i in stops:
    
    up = i[0]
    down = i[1]
    total = total + up - down

    print('Suben {} y bajan {}'.format(up, down))

    print(total)
    n_personas.append(total)
    print(n_personas)

print(n_stops)
print(n_personas)


###### FALTA ESTADÍSITCA

# Average

u = 0
for i in n_personas:
    u +=i

average = u/(len(n_personas))

print(average)


#Standar desviation

s= 0

for i in n_personas:
    
    s += (i-average)**2

std_dev = (s/len(n_personas))**0.5


print(std_dev)