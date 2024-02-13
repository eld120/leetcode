'''
Which teams have made it to the NBA finals but have never won?
'''

import csv

from typing import Set


def never_won_nba_finals()-> Set:
    with open('./nba_finals.csv', 'r') as file:
        reader = csv.DictReader(file)
       
        winners = set()
        losers = set()
        for line in reader:
           
            winners.add(line['Winner'])
            losers.add(line['Loser'])
    print(losers -  winners)
    
    return losers - winners



if __name__ == '__main__':
    never_won_nba_finals()