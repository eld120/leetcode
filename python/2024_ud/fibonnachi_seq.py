
'''
given a number n, ret the nth seq in the sequence
0, 1, 1, 2, 3, 5, 8, 13, 21
'''

memo = dict()
def fibonnaci(n: int)-> int:
    if n in memo:
        return memo[n]
    
    elif n == 0 or n == 1:
        memo[n] = n
        return n
    
    result = fibonnaci(n-1) + fibonnaci(n-2)
    memo[n] = result
    return result


def test_fib_two():
    assert fibonnaci(2) == 1
    assert fibonnaci(5) == 5
    assert fibonnaci(8) == 21