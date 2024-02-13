'''
Write a function that takes as an argument a team name and returns an array of all of the years the team has won the NBA finals.
'''
import csv

from typing import List


def find_wins(team:str)-> List[str]:
    
    with open('./nba_finals.csv', 'r') as file:
        reader = csv.DictReader(file)
        nba_finals_data = dict()
        for line in reader:
            if line['Winner'] in nba_finals_data.keys():
                nba_finals_data[line['Winner']] += f'{line["Year"].strip()},'
            else:
                nba_finals_data[line['Winner']] = f'{line["Year"].strip()},'
        if team not in nba_finals_data.keys():
            return ['Sorry not found']
    return nba_finals_data[team].rstrip(',').split(',')
    

def test_bulls():
    assert find_wins('Chicago Bulls') == ['1998', '1997', '1996', '1993', '1992', '1991']

def test_celtics():
    assert find_wins('Boston Celtics') == ['2008', '1986', '1984', '1981', '1976', '1974', '1969', '1968', '1966', '1965', '1964', '1963', '1962', '1961', '1960', '1959', '1957']

def test_fake():
    assert find_wins('Canadian Moose') == ['Sorry not found']

def test_okc():
    assert find_wins('Oklahoma City Thunder') == ['Sorry not found']

def test_mavericks():
    assert find_wins('Dallas Mavericks') == ['2011']