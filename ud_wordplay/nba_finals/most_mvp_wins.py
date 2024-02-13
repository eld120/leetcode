'''
[ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>
'''
import csv

from collections import Counter

if __name__ == '__main__':
    with open('./nba_finals.csv', 'r') as file:
        reader = csv.DictReader(file)
        mvp_winners = dict()
        for line in reader:
            if line['MVP'] in mvp_winners.keys():
                mvp_winners[line['MVP']][0] += 1
            elif line['MVP'] == '':
                continue
            else:
                mvp_winners[line['MVP']]= [1,line['MVP']]
                

    for value in reversed(sorted(mvp_winners.values())):
        print(f'{value[0]} times: {value[1]}')
