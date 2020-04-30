temperatures_C = [33, 66, 65, 0, 59, 60, 
                62, 64, 70, 76, 80, 81, 80, 
                83, 90, 79, 61, 53, 50, 49, 
                53, 48, 45, 39]

min_temp = min(temperatures_C)
max_temp = max(temperatures_C)
high_temp = [t for t in temperatures_C if t > 70]
avg_temp = sum(temperatures_C)/len(temperatures_C)

corrected_3 = (temperatures_C[2] + temperatures_C[4])/2

temperatures_C[3] = corrected_3

print('Corrected temperatures after estimation: {}'.format(temperatures_C))


temperatures_F = [round((t*1.8)+32, 2) for t in temperatures_C]

if len(high_temp)>4 and max_temp > 80 or avg_temp > 65:
    print('El sistema necesita mantenimiento.')
else:
    print('Todo funciona correctamente.')


###############################

time_temp = {}
hot_hours = {}
hour_count = 0

for h in range(0, len(temperatures_C)):
    time_temp[h] = temperatures_C[h]

for h, t in time_temp.items():
    if time_temp[h] > 70:
        hour_count += 1
        hot_hours[h] = t
    else: 
        if hour_count >= 4:
            break
        else:                
            hour_count = 0
            hot_hours = {}

print(hot_hours)

# if len(hot_hours) >= 4 or avg_temp > 65 or max_temp > 80:
#     print('Se ha desconectado el sistema por superar dtemperatures_C = [33, 66, 65, 0, 59, 60, 
#                 62, 64, 70, 76, 80, 81, 80, 
#                 83, 90, 79, 61, 53, 50, 49, 
#                 53, 48, 45, 39]

min_temp = min(temperatures_C)
max_temp = max(temperatures_C)
high_temp = [t for t in temperatures_C if t > 70]
avg_temp = sum(temperatures_C)/len(temperatures_C)

### Cómo se hace la estimación para las 3 am????

temperatures_F = [round((t*1.8)+32, 2) for t in temperatures_C]

if len(high_temp)>4 and max_temp > 0 or avg_temp > 65:
    print('El sistema necesita mantenimiento.')
else:
    print('Todo funciona correctamente.')

hot_hours = hot_hours = [temperatures_C.index(i) for i in temperatures_C if i >= 70]


print('Las horas más calurosas son: '.format(hot_hours))


###############################

time_temp = {}
hot_hours = {}
hour_count = 0

for h in range(0, len(temperatures_C)):
    time_temp[h] = temperatures_C[h]

for h, t in time_temp.items():
    if time_temp[h] > 70:
        hour_count += 1
        hot_hours[h] = t
    else: 
        if hour_count >= 4:
            break
        else:                
            hour_count = 0
            hot_hours = {}

print(hot_hours)

if len(hot_hours) >= 4 or avg_temp > 65 or max_temp > 80:
    print('Se ha desconectado el sistema por superar durante {} horas la Tª máx. establecida'.format(len(hot_hours)))

########################################
'''
4. Find the average value of the temperature lists (ºC and ºF). What is the relation between both average values?

5. Find the standard deviation of the temperature lists (ºC and ºF). What is the relation between both standard deviations?
'''
######################      CREAR OBJETO CALDERA E INTENTAR HACERLO CON LOS ATRIBUTOS!





