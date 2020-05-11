import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

print(data)

 # Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.

first_innings_deliveries = data['innings'][0]['1st innings']['deliveries']
count_deliveries =0 
for faced in first_innings_deliveries:
     for delivery_number, delivery_info in faced.items():
            if delivery_info['batsman'] == 'SC Ganguly':
                count_deliveries += 1
print('The deliveries faced by SC Ganguly was :',count_deliveries)

#  Who was man of the match and how many runs did he scored ?

man_of_the_match = data['info']['player_of_match']
print('Player of the match is : ' + man_of_the_match[0])
runs_scored = 0
for runs in first_innings_deliveries:
    for delivery_number, delivery_info in runs.items():
        if delivery_info['batsman'] == 'BB McCullum':
            runs_scored += delivery_info['runs']['batsman']
print('Total Runs scored by ' + man_of_the_match[0] + ' is :', runs_scored)

#  Which batsman played in the first inning?

batsman =[]
for all_batsman in first_innings_deliveries:
    for delivery_number, delivery_info in all_batsman.items():
        batsman.append(delivery_info['batsman'])
print('All the batsman who played in first ininng are :', set(batsman))

# Which batsman had the most no. of sixes in first inning ?

most_sixes = []
for sixes in first_innings_deliveries:
    for delivery_number, delivery_info in sixes.items():
        if 'runs' in delivery_info and delivery_info['runs']['batsman'] == 6:
            most_sixes.append(delivery_info['batsman'])

batsman_sixes = Counter(most_sixes)

# Find the names of all players that got bowled out in the second innings.

second_innings_deliveries = data['innings'][1]['2nd innings']['deliveries']
bowled_players = []
for bowled_out in second_innings_deliveries:
    for delivery_number, delivery_info in bowled_out.items():
        if 'wicket' in delivery_info and delivery_info['wicket']['kind'] == 'bowled':
            bowled_players.append(delivery_info['wicket']['player_out'])
print(bowled_players)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?

extras_1st_innings = [delivery_info 
                      for delivery in first_innings_deliveries 
                      for delivery_number, delivery_info in delivery.items() 
                      if 'extras' in delivery_info]

extras_2nd_innings = [delivery_info 
                      for delivery in second_innings_deliveries 
                      for delivery_number, delivery_info in delivery.items() 
                      if 'extras' in delivery_info]

difference = len(extras_1st_innings) - len(extras_2nd_innings)
print(difference)

# Code ends here 
