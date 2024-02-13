'''
Write a function that takes as an argument a year and returns the winner of the NBA finals that year.
'''

def find_nba_finals_winner(year: int)-> str:
    with open('./nba_finals.csv', 'r') as f:
        for line in f:
            if line[:4] == str(year):
                winner = line.split(',')
                return winner[1]
            

def test_2005():
    assert find_nba_finals_winner(2005) == 'San Antonio Spurs'

def test_1998():
    assert find_nba_finals_winner(1998) == 'Chicago Bulls'

def test_1992():
    assert find_nba_finals_winner(1992) == 'Chicago Bulls'

def test_1985():
    assert find_nba_finals_winner(1985) == 'Los Angeles Lakers'