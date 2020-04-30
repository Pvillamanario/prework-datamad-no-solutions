points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

def dist_center (a,b):
    
    return ((a**2 + b**2)**(1/2))

multiple_impacts = []

for i in points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

def dist_center (a,b):
    
    return ((a**2 + b**2)**(1/2))

multiple_impacts = []

for i in points:
    if points.count(i) >= 2 and i not in multiple_impacts:
        multiple_impacts.append(i)

for i in multiple_impacts:
    print('Hay {} impactos en las coordenadas {}!\n'.format(points.count(i),i))
    
################

sup_d = []
sup_i = []
inf_d = []
inf_i = []

for i in points:
    if i[0] > 0 and i[1] > 0:
        sup_d.append(i)

    elif i[0] < 0 and  i[1] > 0:
        sup_i.append(i)
    
    elif i[0] > 0 and  i[1] < 0:
        inf_d.append(i)

    elif i[0] < 0 and  i[1] < 0:
        inf_i.append(i)
    
    else:
        pass

print('Las flechas han caído así:\n')
print('En el cuadrante superior derecho:     {}'.format(len(sup_d)))
print('En el cuadrante superior izquierdo:   {}'.format(len(sup_i)))
print('En el cuadrante inferior derecho:     {}'.format(len(inf_d)))
print('En el cuadrante inferior izquierdo:   {}'.format(len(inf_i)))

##########################

distances = {}
min_dist = 100
r = 9
for i in points:
    if i not in distances.items():
        distances[i]=dist_center(i[0], i[1])

# for k in distances:
#     print(k, distances[k])

for v in distances.values():
    if v < min_dist:
        min_dist = v

for k,v in distances.items():
    if v == min_dist:
        print('La flecha en {} ha sido de las mejores'.format(k))

print('La distancia al centro de los mejores tiros ha sido {}\n'.format(min_dist))

for k,v in distances.items():
    if v > 9:
        print('La flecha en {} se ha salido de la diana'.format(k))