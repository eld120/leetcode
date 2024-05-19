from collections import deque


def baseball_something(operations: list[str]) -> int:
    stack = deque()
    score = 0
    for todo in operations:
        breakpoint()
        if todo == "+":
            score1 = int(stack.pop())
            score2 = int(stack.pop())
            score = score1 + score2
            stack.append(score)
        elif todo == "D":
            score = score * score
            stack.append(score)
        elif todo == "C":
            stack.pop()
        else:
            score += int(todo)
            stack.append([score, int(todo)])
    #breakpoint()
    new_score = 0
    while stack:
        new_score += stack.pop()

    return new_score


def base_ball_game_or_something(operations: list[str]) -> int:
    stack = deque()
    score = 0
    for val in operations:
        if val == '+':
            most_recent_score, value_1 = stack.pop()
            second_score, value_2 = stack.pop()
            new_score = most_recent_score + second_score
            stack.append([second_score, value_2] )
            stack.append([most_recent_score, value_1])
            stack.append([new_score, value_1+ value_2])
        elif val == 'D':
            most_recent_score, value_1 = stack.pop()
            stack.append([most_recent_score, value_1])
            stack.append([most_recent_score * 2, value_1 * 2])
        elif val == 'C':
            stack.pop()
        else:
            stack.append([int(val), int(val)])
    
    while stack:
        one, two  = stack.pop()
        score += one
    return score


def test_one():
    assert base_ball_game_or_something(["5", "2", "C", "D", "+"]) == 30
