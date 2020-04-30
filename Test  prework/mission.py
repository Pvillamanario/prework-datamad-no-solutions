dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

above_trshld = [i for i in dbs if i > 10]

print(above_trshld)

##############

time = []

for i in range(0,len(dbs)):

       if dbs[i] > 10:
              time.append(i)

print(time)

##############

moments = []

for i in enumerate(dbs):
       if i[1] > 10:
              moments.append(i)

print(moments)

##############

counter = 0

while counter < 2:
    
       for i in dbs:
              if i > 10:
                     counter += 1
              else:
                     pass
       
       if counter < 2:
              pass

       else:
              print('Alarm!!')

##############    

hacked_dbs = []

for i in dbs:
       if i > 20 and i < 30:
              i = i - 12
              hacked_dbs.append(i)

       elif i > 30:
              i = i - 18
              hacked_dbs.append(i)
       else:
              hacked_dbs.append(i)

print(hacked_dbs)

