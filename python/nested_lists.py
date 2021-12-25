if __name__ == '__main__':

    lst = [100,100]
    names = []
    scoreboard = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append([name, score])
        scoreboard.append(score)
    scoreboard.sort()
    for val in scoreboard:
        if val <= lst[0]:
            lst[0] = val
        elif val < lst[1] and val > lst[0]:
            lst[1] = val
        
    answers = []
    for val in names:
        if val[1] == lst[1]:
            answers.append(val[0])
    answers.sort()
    [print(name) for name in answers]