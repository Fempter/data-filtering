# -*- coding: utf-8 -*-

import csv
import numpy as np
import datetime
import pandas as pd

csvfile = open('abpm_test.csv', 'r')
dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',"')
csvfile.seek(0)
reader = csv.reader(csvfile, dialect)

def percentage(pressure_table, more_than):
    counter = 0
    for pressure in pressure_table:
        if pressure > more_than:
            counter += 1
    whole = len(pressure_table)
    return 100*float(counter)/float(whole)

def dipping(sleep_time, wake_time):
    return 100*((wake_time-sleep_time)/wake_time)

def all_indices(value, qlist):
    indices = []
    for i, member in enumerate(qlist):
        if value == member:
            indices.append(i)
    return indices

def mean_value_for_ms(main_dataframe, custom_dataframe, minimum_value_from_custom_dataframe, col_name):
    idx = custom_dataframe.loc[lambda s: s == minimum_value_from_custom_dataframe]
    idx = idx[idx == minimum_value_from_custom_dataframe].index.tolist()
    means = []
    for i in idx:
        pos = main_dataframe.index.get_loc(i)
        df1 = main_dataframe.iloc[max(pos-1,0): min(pos+2,len(main_dataframe.index))]
        if col_name == 'sys':
            means.append(np.mean(df1.sys))
        elif col_name == 'dia':
            means.append(np.mean(df1.dia))
        elif col_name == 'map':
            means.append(np.mean(df1.map))
    if len(means) > 1:
        return np.min(means)
    elif len(means) == 1:
        return means[0]
    
def morning_surge(morning_2h_value, sleep_mean_value):
    return (morning_2h_value-sleep_mean_value)

patient_info = []
wake_sleep_times = []
patient_measures = []

DATE = []
TIME = []
DATE_TIME = []
SYS = []
DIA = []
PUL = []
MAP = []

for i, row in enumerate(reader):
    if 0 < i <= 1:
        name, sex, age = row
        patient_info.append(tuple(row))
    if 2 < i <= 3:
        sleep, wake = row
        wake_sleep_times.append(tuple(row))
    if i > 4:
        date, time, sys, dia, pul, err, exc = row
        if row[5] == '0' and row[6] == '0':
            #patient_measures.append(tuple((date, time, int(sys), int(dia), int(pul))))
            map_ = int(float(dia) + (1/3.)*(float(sys)-float(dia)))
            #date = datetime.strptime(date, "%Y-%m-%d").date()
            #time = datetime.strptime(time, "%H:%M").time()
            DATE.append(date)
            TIME.append(time)
            SYS.append(int(sys))
            DIA.append(int(dia))
            PUL.append(int(pul))
            MAP.append(map_)

for i in wake_sleep_times:
    sleep_time_hour = datetime.datetime.strptime(i[0], '%H:%M').time()
    wake_time_hour = datetime.datetime.strptime(i[1], '%H:%M').time()

for i in map(list,zip(DATE,TIME)):
    DATE_TIME.append(i[0]+' '+i[1])

data = dict()
data['datetime'] = DATE_TIME
data['sys'] = SYS
data['dia'] = DIA
data['pul'] = PUL
data['map'] = MAP

df = pd.DataFrame(data, columns = ['datetime','sys','dia','pul','map'])
df['datetime'] = pd.to_datetime(df['datetime'])

df = df.set_index('datetime')



###############################ALL TIME###############################
df

all_time_sys_mean = np.mean(df['sys'])
all_time_dia_mean = np.mean(df['dia'])
all_time_pul_mean = np.mean(df['pul'])
all_time_map_mean = np.mean(df['map'])

all_time_sys_std = np.std(df['sys'])
all_time_dia_std = np.std(df['dia'])
all_time_pul_std = np.std(df['pul'])
all_time_map_std = np.std(df['map'])

###############################WAKE TIME###############################
wake_time = df.between_time(wake_time_hour,sleep_time_hour)

wake_time_sys_mean = np.mean(wake_time['sys'])
wake_time_dia_mean = np.mean(wake_time['dia'])
wake_time_pul_mean = np.mean(wake_time['pul'])
wake_time_map_mean = np.mean(wake_time['map'])

wake_time_sys_std = np.std(wake_time['sys'])
wake_time_dia_std = np.std(wake_time['dia'])
wake_time_pul_std = np.std(wake_time['pul'])
wake_time_map_std = np.std(wake_time['map'])

wake_time_sys_min = np.min(wake_time['sys'])
wake_time_dia_min = np.min(wake_time['dia'])
wake_time_pul_min = np.min(wake_time['pul'])
wake_time_map_min = np.min(wake_time['map'])

wake_time_sys_max = np.max(wake_time['sys'])
wake_time_dia_max = np.max(wake_time['dia'])
wake_time_pul_max = np.max(wake_time['pul'])
wake_time_map_max = np.max(wake_time['map'])

###############################SLEEP TIME###############################
delta_one_second = datetime.timedelta(seconds=1)

time1 = ((datetime.datetime.combine(datetime.date(1, 1, 1), sleep_time_hour))+delta_one_second).time()
time2 = ((datetime.datetime.combine(datetime.date(1, 1, 1), wake_time_hour))-delta_one_second).time()

sleep_time = df.between_time(time1,time2)

sleep_time_sys_mean = np.mean(sleep_time['sys'])
sleep_time_dia_mean = np.mean(sleep_time['dia'])
sleep_time_pul_mean = np.mean(sleep_time['pul'])
sleep_time_map_mean = np.mean(sleep_time['map'])

sleep_time_sys_std = np.std(sleep_time['sys'])
sleep_time_dia_std = np.std(sleep_time['dia'])
sleep_time_pul_std = np.std(sleep_time['pul'])
sleep_time_map_std = np.std(sleep_time['map'])

sleep_time_sys_min = np.min(sleep_time['sys'])
sleep_time_dia_min = np.min(sleep_time['dia'])
sleep_time_pul_min = np.min(sleep_time['pul'])
sleep_time_map_min = np.min(sleep_time['map'])

sleep_time_sys_max = np.max(sleep_time['sys'])
sleep_time_dia_max = np.max(sleep_time['dia'])
sleep_time_pul_max = np.max(sleep_time['pul'])
sleep_time_map_max = np.max(sleep_time['map'])

###############################FIRST 3 MEASURES###############################
first_three_measures = df.head(3)

first_three_measures_sys_mean = np.mean(first_three_measures['sys'])
first_three_measures_dia_mean = np.mean(first_three_measures['dia'])
first_three_measures_pul_mean = np.mean(first_three_measures['pul'])
first_three_measures_map_mean = np.mean(first_three_measures['map'])

first_three_measures_sys_std = np.std(first_three_measures['sys'])
first_three_measures_dia_std = np.std(first_three_measures['dia'])
first_three_measures_pul_std = np.std(first_three_measures['pul'])
first_three_measures_map_std = np.std(first_three_measures['map'])

###############################2H AFTER WAKE TIME###############################
delta_two_hours = datetime.timedelta(hours=2)

time3 = ((datetime.datetime.combine(datetime.date(1, 1, 1), wake_time_hour))+delta_two_hours).time()

two_h_after_wake_time = df.between_time(wake_time_hour,time3)

two_h_after_wake_time_sys_mean = np.mean(two_h_after_wake_time['sys'])
two_h_after_wake_time_dia_mean = np.mean(two_h_after_wake_time['dia'])
two_h_after_wake_time_pul_mean = np.mean(two_h_after_wake_time['pul'])
two_h_after_wake_time_map_mean = np.mean(two_h_after_wake_time['map'])

two_h_after_wake_time_sys_min = np.min(two_h_after_wake_time['sys'])
two_h_after_wake_time_dia_min = np.min(two_h_after_wake_time['dia'])
two_h_after_wake_time_pul_min = np.min(two_h_after_wake_time['pul'])
two_h_after_wake_time_map_min = np.min(two_h_after_wake_time['map'])

###############################MORNING SURGE###############################
sleep_time_sys_min_mean = mean_value_for_ms(df, sleep_time.sys, sleep_time_sys_min, 'sys')
sleep_time_dia_min_mean = mean_value_for_ms(df, sleep_time.dia, sleep_time_dia_min, 'dia')
sleep_time_map_min_mean = mean_value_for_ms(df, sleep_time.map, sleep_time_map_min, 'map')

morning_surge_sys = morning_surge(two_h_after_wake_time_sys_mean, sleep_time_sys_min_mean)
morning_surge_dia = morning_surge(two_h_after_wake_time_dia_mean, sleep_time_dia_min_mean)
morning_surge_map = morning_surge(two_h_after_wake_time_map_mean, sleep_time_map_min_mean)




###############################PRINTING EXERCISES###############################

print '\nCzęść a) \n'
print '\tMEAN\tSTD'
print   'SYS\t', "%.2f" % all_time_sys_mean, '\t', "%.2f" % all_time_sys_std, '\n',\
        'DIA\t', "%.2f" % all_time_dia_mean, '\t', "%.2f" % all_time_dia_std, '\n',\
        'PUL\t', "%.2f" % all_time_pul_mean, '\t', "%.2f" % all_time_pul_std, '\n',\
        'MAP\t', "%.2f" % all_time_map_mean, '\t', "%.2f" % all_time_map_std, '\n'

print '\nCzęść b) \n \n', "%.2f" % percentage(df['sys'], 130), '%\n'
print '\nCzęść c) \n \n', "%.2f" % percentage(df['dia'], 80), '%\n'

print '\nCzęść d) \n'
print '\tMEAN\tSTD\tMIN\tMAX'
print   'SYS\t', "%.2f" % sleep_time_sys_mean, '\t', "%.2f" % sleep_time_sys_std, '\t', sleep_time_sys_min, '\t', sleep_time_sys_max, '\n',\
        'DIA\t', "%.2f" % sleep_time_dia_mean, '\t', "%.2f" % sleep_time_dia_std, '\t', sleep_time_dia_min, '\t', sleep_time_dia_max, '\n',\
        'PUL\t', "%.2f" % sleep_time_pul_mean, '\t', "%.2f" % sleep_time_pul_std, '\t', sleep_time_pul_min, '\t', sleep_time_pul_max, '\n',\
        'MAP\t', "%.2f" % sleep_time_map_mean, '\t', "%.2f" % sleep_time_map_std, '\t', sleep_time_map_min, '\t', sleep_time_map_max, '\n'

print '\nCzęść e) \n \n', "%.2f" % percentage(sleep_time['sys'], 120), '%\n'
print '\nCzęść f) \n \n', "%.2f" % percentage(sleep_time['dia'], 70), '%\n'

print '\nCzęść g) \n'
print '\tMEAN\tSTD\tMIN\tMAX'
print   'SYS\t', "%.2f" % wake_time_sys_mean, '\t', "%.2f" % wake_time_sys_std, '\t', wake_time_sys_min, '\t', wake_time_sys_max, '\n',\
        'DIA\t', "%.2f" % wake_time_dia_mean, '\t', "%.2f" % wake_time_dia_std, '\t', wake_time_dia_min, '\t', wake_time_dia_max, '\n',\
        'PUL\t', "%.2f" % wake_time_pul_mean, '\t', "%.2f" % wake_time_pul_std, '\t', wake_time_pul_min, '\t', wake_time_pul_max, '\n',\
        'MAP\t', "%.2f" % wake_time_map_mean, '\t', "%.2f" % wake_time_map_std, '\t', wake_time_map_min, '\t', wake_time_map_max, '\n'

print '\nCzęść h) \n \n', "%.2f" % percentage(wake_time['sys'], 120), '%\n'
print '\nCzęść i) \n \n', "%.2f" % percentage(wake_time['dia'], 70), '%\n'

print '\nCzęść j) \n'
print '\tMEAN\tSTD'
print   'SYS\t', "%.2f" % first_three_measures_sys_mean, '\t', "%.2f" % first_three_measures_sys_std, '\n',\
        'DIA\t', "%.2f" % first_three_measures_dia_mean, '\t', "%.2f" % first_three_measures_dia_std, '\n',\
        'PUL\t', "%.2f" % first_three_measures_pul_mean, '\t', "%.2f" % first_three_measures_pul_std, '\n',\
        'MAP\t', "%.2f" % first_three_measures_map_mean, '\t', "%.2f" % first_three_measures_map_std, '\n'

print '\nCzęść k) \n'
print '\tMORNING SURGE'
print   'SYS\t', "%.2f" % morning_surge_sys, '\n',\
        'DIA\t', "%.2f" % morning_surge_dia, '\n',\
        'MAP\t', "%.2f" % morning_surge_map, '\n'

print '\nCzęść l) \n'
print '\tDIPPING'
print   'SYS\t', "%.2f" % dipping(sleep_time_sys_mean,wake_time_sys_mean), '\n',\
        'DIA\t', "%.2f" % dipping(sleep_time_dia_mean,wake_time_dia_mean), '\n',\
        'MAP\t', "%.2f" % dipping(sleep_time_map_mean,wake_time_map_mean), '\n'
