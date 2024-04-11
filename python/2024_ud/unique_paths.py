from collections import deque



def count_paths(m: int, n: int) -> int:
    '''Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.'''
    deck = deque()
    counter = 0
    
    y,x = 0,0
    deck.append((y,x))
    while len(deck) > 0:
        #breakpoint()
        temp = deck.pop()
        x = temp[1]
        y = temp[0]
        if x in range(0,n) and y in range(0, m) :

            deck.append((y, x+1))
            deck.append((y + 1, x))
        if temp == (m-1, n-1):
            counter += 1
    return counter


def something(m, n):
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[-1][-1]

def test_one():
    assert count_paths(3, 2) == 3
    assert something(3, 2) == 3

def test_two():
    assert count_paths(3,7) == 28
    assert something(3,7) == 28

def test_time_limit():
    assert something(23,12) == 193536720
    assert count_paths(23,12) == 193536720

