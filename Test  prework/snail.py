well_height=125
daily_distance=30
nigth_distance=20
snail_position=0

days = 0

while snail_position < 125:
    snail_position += daily_distance
    days += 1

    if snail_position >= well_height:
        print('Ha salido del pozo en {} días\n'.format(days))
        break
    else:
        snail_position -= nigth_distance
    
        


############################################################

well_height=125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nigth_distance=20
snail_position=0




    
while snail_position < 125:
    
    for cm in advance_cm:

        days += 1
        snail_position += cm

        if snail_position >= well_height:
            print('Days = {}'.format(days))
            break

        else:
            snail_position -= nigth_distance
        
            

print('La distancia máxima que avanza será de {} cm.'.format(max(advance_cm[:days])-nigth_distance))
print('La distancia mínima que avanza será de {} cm.'.format(min(advance_cm[:days])-nigth_distance))



# print('El avance medio diario es de {} cm.'.format((advance_cm[:days])/days))
